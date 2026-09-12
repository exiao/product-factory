#!/usr/bin/env python3
"""
Fetch all PR conversation comments + reviews + review threads (inline threads)
for the PR associated with the current git branch, by shelling out to:

  gh api graphql

Requires:
  - `gh auth login` already set up
  - current branch has an associated (open) PR

Usage:
  python fetch_comments.py > pr_comments.json

This is a modified copy of OpenAI's `skills/gh-address-comments` helper
(Apache-2.0). Local changes add base-repository lookup from the PR URL,
independent connection pagination, and an explicit nested-comment truncation
error.
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any
from urllib.parse import urlparse

QUERY = """\
query(
  $owner: String!,
  $repo: String!,
  $number: Int!,
  $commentsCursor: String,
  $reviewsCursor: String,
  $threadsCursor: String
) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $number) {
      number
      url
      title
      state

      # Top-level "Conversation" comments (issue comments on the PR)
      comments(first: 100, after: $commentsCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          body
          createdAt
          updatedAt
          author { login }
        }
      }

      # Review submissions (Approve / Request changes / Comment), with body if present
      reviews(first: 100, after: $reviewsCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          state
          body
          submittedAt
          author { login }
        }
      }

      # Inline review threads (grouped), includes resolved state
      reviewThreads(first: 100, after: $threadsCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          isResolved
          isOutdated
          path
          line
          diffSide
          startLine
          startDiffSide
          originalLine
          originalStartLine
          resolvedBy { login }
          comments(first: 100) {
            pageInfo { hasNextPage }
            nodes {
              id
              body
              createdAt
              updatedAt
              author { login }
            }
          }
        }
      }
    }
  }
}
"""


def _run(cmd: list[str], stdin: str | None = None) -> str:
    p = subprocess.run(cmd, input=stdin, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{p.stderr}")
    return p.stdout


def _run_json(cmd: list[str], stdin: str | None = None) -> dict[str, Any]:
    out = _run(cmd, stdin=stdin)
    try:
        return json.loads(out)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse JSON from command output: {e}\nRaw:\n{out}") from e


def _ensure_gh_authenticated() -> None:
    try:
        _run(["gh", "auth", "status"])
    except RuntimeError:
        print("run `gh auth login` to authenticate the GitHub CLI", file=sys.stderr)
        raise RuntimeError("gh auth status failed; run `gh auth login` to authenticate the GitHub CLI") from None


def gh_pr_view_json(fields: str) -> dict[str, Any]:
    # fields is a comma-separated list like: "number,url"
    return _run_json(["gh", "pr", "view", "--json", fields])


def get_current_pr_ref() -> tuple[str, str, int]:
    """
    Resolve the PR for the current branch (whatever gh considers associated).
    Use the PR URL so GraphQL is queried against the base repository. This is
    important for PRs opened from a fork: the head repository is not where the
    PR itself lives.
    """
    pr = gh_pr_view_json("number,url")
    url = pr.get("url")
    if not isinstance(url, str) or not url:
        raise RuntimeError("gh pr view did not return a PR URL")

    path_parts = [part for part in urlparse(url).path.split("/") if part]
    if len(path_parts) < 4 or path_parts[-2] != "pull":
        raise RuntimeError(f"Could not parse base repository and PR number from URL: {url}")
    owner, repo = path_parts[-4], path_parts[-3]
    try:
        number = int(path_parts[-1])
    except ValueError as e:
        raise RuntimeError(f"Could not parse PR number from URL: {url}") from e
    return owner, repo, number


def gh_api_graphql(
    owner: str,
    repo: str,
    number: int,
    comments_cursor: str | None = None,
    reviews_cursor: str | None = None,
    threads_cursor: str | None = None,
) -> dict[str, Any]:
    """
    Call `gh api graphql` using -F variables, avoiding JSON blobs with nulls.
    Query is passed via stdin using query=@- to avoid shell newline/quoting issues.
    """
    cmd = [
        "gh",
        "api",
        "graphql",
        "-F",
        "query=@-",
        "-F",
        f"owner={owner}",
        "-F",
        f"repo={repo}",
        "-F",
        f"number={number}",
    ]
    if comments_cursor:
        cmd += ["-F", f"commentsCursor={comments_cursor}"]
    if reviews_cursor:
        cmd += ["-F", f"reviewsCursor={reviews_cursor}"]
    if threads_cursor:
        cmd += ["-F", f"threadsCursor={threads_cursor}"]

    return _run_json(cmd, stdin=QUERY)


def fetch_all(owner: str, repo: str, number: int) -> dict[str, Any]:
    conversation_comments: list[dict[str, Any]] = []
    reviews: list[dict[str, Any]] = []
    review_threads: list[dict[str, Any]] = []
    seen_comment_ids: set[str] = set()
    seen_review_ids: set[str] = set()
    seen_thread_ids: set[str] = set()

    comments_cursor: str | None = None
    reviews_cursor: str | None = None
    threads_cursor: str | None = None
    comments_done = False
    reviews_done = False
    threads_done = False

    pr_meta: dict[str, Any] | None = None

    while True:
        payload = gh_api_graphql(
            owner=owner,
            repo=repo,
            number=number,
            comments_cursor=comments_cursor,
            reviews_cursor=reviews_cursor,
            threads_cursor=threads_cursor,
        )

        if "errors" in payload and payload["errors"]:
            raise RuntimeError(f"GitHub GraphQL errors:\n{json.dumps(payload['errors'], indent=2)}")

        pr = payload["data"]["repository"]["pullRequest"]
        if pr_meta is None:
            pr_meta = {
                "number": pr["number"],
                "url": pr["url"],
                "title": pr["title"],
                "state": pr["state"],
                "owner": owner,
                "repo": repo,
            }

        c = pr["comments"]
        r = pr["reviews"]
        t = pr["reviewThreads"]

        # The GraphQL query always includes all three connections. Once a
        # shorter connection is exhausted, its nullable cursor would otherwise
        # reset it to page one on every later request. Ignore that connection's
        # repeated first page while the longer connections continue, and also
        # deduplicate by ID as a second line of defense.
        if not comments_done:
            for node in c.get("nodes") or []:
                node_id = node.get("id")
                if node_id is None or node_id not in seen_comment_ids:
                    conversation_comments.append(node)
                    if node_id is not None:
                        seen_comment_ids.add(node_id)
            comments_page = c["pageInfo"]
            if comments_page["hasNextPage"]:
                comments_cursor = comments_page.get("endCursor")
                if not comments_cursor:
                    raise RuntimeError("GitHub returned hasNextPage for comments without an endCursor")
            else:
                comments_done = True
                comments_cursor = None

        if not reviews_done:
            for node in r.get("nodes") or []:
                node_id = node.get("id")
                if node_id is None or node_id not in seen_review_ids:
                    reviews.append(node)
                    if node_id is not None:
                        seen_review_ids.add(node_id)
            reviews_page = r["pageInfo"]
            if reviews_page["hasNextPage"]:
                reviews_cursor = reviews_page.get("endCursor")
                if not reviews_cursor:
                    raise RuntimeError("GitHub returned hasNextPage for reviews without an endCursor")
            else:
                reviews_done = True
                reviews_cursor = None

        if not threads_done:
            for thread in t.get("nodes") or []:
                nested_page = (thread.get("comments") or {}).get("pageInfo") or {}
                if nested_page.get("hasNextPage"):
                    raise RuntimeError(
                        "Review thread "
                        f"{thread.get('id', '<unknown>')} has more than 100 comments; "
                        "refusing to return truncated nested comments"
                    )
                thread_id = thread.get("id")
                if thread_id is None or thread_id not in seen_thread_ids:
                    review_threads.append(thread)
                    if thread_id is not None:
                        seen_thread_ids.add(thread_id)
            threads_page = t["pageInfo"]
            if threads_page["hasNextPage"]:
                threads_cursor = threads_page.get("endCursor")
                if not threads_cursor:
                    raise RuntimeError("GitHub returned hasNextPage for review threads without an endCursor")
            else:
                threads_done = True
                threads_cursor = None

        if comments_done and reviews_done and threads_done:
            break

    assert pr_meta is not None
    return {
        "pull_request": pr_meta,
        "conversation_comments": conversation_comments,
        "reviews": reviews,
        "review_threads": review_threads,
    }


def main() -> None:
    _ensure_gh_authenticated()
    owner, repo, number = get_current_pr_ref()
    result = fetch_all(owner, repo, number)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
