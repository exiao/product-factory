#!/usr/bin/env python3
"""Review recorded skill experiments locally; never launches models or installs candidates."""
import argparse
import html
import json
import math
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def analyze(data):
    require(isinstance(data, dict), 'input must be an object')
    require(data.get('schema_version') == 1, 'schema_version must be 1')
    baseline = data.get('baseline')
    candidates = data.get('candidates')
    require(isinstance(candidates, list) and len(candidates) >= 2, 'need baseline and at least one candidate')
    require(all(isinstance(c, str) and c for c in candidates), 'candidate IDs must be nonempty strings')
    require(len(set(candidates)) == len(candidates) and baseline in candidates, 'unique candidates must include baseline')
    cases = data.get('cases')
    require(isinstance(cases, list) and cases, 'cases must be a nonempty list')
    index = {}
    for case in cases:
        require(isinstance(case, dict), 'each case must be an object')
        key = case.get('id')
        require(isinstance(key, str) and key and key not in index, 'case IDs must be unique nonempty strings')
        require(case.get('split') in ('train', 'validation', 'test'), f'{key}: invalid split')
        require(type(case.get('critical', False)) is bool, f'{key}: critical must be boolean')
        require(type(case.get('repetitions', 1)) is int and case.get('repetitions', 1) > 0, f'{key}: repetitions must be positive integer')
        if 'should_trigger' in case:
            require(type(case['should_trigger']) is bool, f'{key}: should_trigger must be boolean')
        index[key] = case
    runs = data.get('runs')
    require(isinstance(runs, list), 'runs must be a list')
    results = {}
    for run in runs:
        require(isinstance(run, dict), 'each run must be an object')
        c, key, rep = run.get('candidate'), run.get('case'), run.get('repeat', 0)
        require(c in candidates and key in index, 'run references unknown candidate/case')
        require(type(rep) is int and 0 <= rep < index[key].get('repetitions', 1), f'{key}: repeat outside declared range')
        k = (c, key, rep)
        require(k not in results, f'duplicate run {k}')
        status = run.get('status')
        require(status in ('ok', 'error', 'skipped'), f'{k}: status must be ok/error/skipped')
        if status == 'ok':
            score = run.get('score')
            require(type(score) in (int, float) and math.isfinite(score) and 0 <= score <= 1, f'{k}: finite score in [0,1] required')
            require(type(run.get('passed')) is bool, f'{k}: passed boolean required')
            require(isinstance(run.get('evidence'), str) and bool(run['evidence'].strip()), f'{k}: evidence reference required')
        if 'triggered' in run:
            require(type(run['triggered']) is bool, f'{k}: triggered must be boolean')
        for field in ('tokens', 'cost', 'seconds'):
            if field in run:
                val = run[field]
                require(type(val) in (int, float) and math.isfinite(val) and val >= 0, f'{k}: invalid {field}')
        results[k] = run
    require(type(data.get('min_pairs')) is int and data['min_pairs'] > 0, 'predeclare positive min_pairs')
    margin = data.get('min_mean_gain')
    require(type(margin) in (int, float) and math.isfinite(margin) and 0 <= margin <= 1, 'predeclare min_mean_gain in [0,1]')
    validation = [(k, r) for k, case in index.items() if case['split'] == 'validation' for r in range(case.get('repetitions', 1))]
    require(bool(validation), 'need validation cases')
    critical = [(k, r) for k, case in index.items() if case.get('critical') and case['split'] != 'test' for r in range(case.get('repetitions', 1))]
    summary = []
    for candidate in candidates:
        if candidate == baseline:
            continue
        missing, critical_failures, differences = [], [], []
        for key, rep in validation:
            a, b = results.get((baseline, key, rep)), results.get((candidate, key, rep))
            if not a or not b or a['status'] != 'ok' or b['status'] != 'ok':
                missing.append(f'{key}#{rep}')
            elif 'should_trigger' in index[key] and ('triggered' not in a or 'triggered' not in b):
                missing.append(f'trigger:{key}#{rep}')
            else:
                differences.append(b['score'] - a['score'])
        for key, rep in critical:
            a, b = results.get((baseline, key, rep)), results.get((candidate, key, rep))
            if not a or not b or a['status'] != 'ok' or b['status'] != 'ok':
                missing.append(f'critical:{key}#{rep}')
            elif not b['passed']:
                critical_failures.append(f'{key}#{rep}')
        mean = sum(differences) / len(differences) if differences else None
        if critical_failures:
            decision = 'reject'
        elif missing or len(differences) < data['min_pairs']:
            decision = 'inconclusive'
        elif mean > margin:
            decision = 'eligible_for_review'
        else:
            decision = 'retain_baseline'
        summary.append({'candidate': candidate, 'decision': decision, 'paired_validation_runs': len(differences), 'mean_gain': mean, 'missing_or_failed': sorted(set(missing)), 'critical_failures': critical_failures})
    # Frontier uses training only; test results never enter candidate selection.
    train = [(k, rep) for k, c in index.items() if c['split'] == 'train' for rep in range(c.get('repetitions', 1))]
    vectors = {}
    for candidate in candidates:
        rs = [results.get((candidate, key, rep)) for key, rep in train]
        if rs and all(r and r['status'] == 'ok' for r in rs):
            vectors[candidate] = [r['score'] for r in rs]
    frontier = [c for c, values in vectors.items() if not any(all(x >= y for x, y in zip(other, values)) and any(x > y for x, y in zip(other, values)) for d, other in vectors.items() if c != d)]
    triggers = {}
    for candidate in candidates:
        counts = dict(tp=0, fp=0, tn=0, fn=0, unknown=0)
        for key, case in index.items():
            if 'should_trigger' not in case or case['split'] == 'test':
                continue
            for rep in range(case.get('repetitions', 1)):
                run = results.get((candidate, key, rep))
                if not run or run['status'] != 'ok' or 'triggered' not in run:
                    counts['unknown'] += 1
                else:
                    expected, observed = case['should_trigger'], run['triggered']
                    counts['tp' if expected and observed else 'fn' if expected else 'fp' if observed else 'tn'] += 1
        if sum(counts.values()):
            counts['precision'] = counts['tp'] / (counts['tp'] + counts['fp']) if counts['tp'] + counts['fp'] else None
            counts['recall'] = counts['tp'] / (counts['tp'] + counts['fn']) if counts['tp'] + counts['fn'] else None
            triggers[candidate] = counts
    costs = {}
    for candidate in candidates:
        rs = [run for (c, key, _), run in results.items() if c == candidate and index[key]['split'] != 'test']
        costs[candidate] = {f: {'recorded_total': sum(r.get(f, 0) for r in rs), 'runs_with_measurement': sum(f in r for r in rs), 'recorded_runs': len(rs)} for f in ('tokens', 'cost', 'seconds')}
    return {'baseline': baseline, 'candidates': summary, 'training_frontier': frontier, 'trigger_metrics': triggers, 'resource_usage': costs, 'test_runs_excluded': sum(index[key]['split'] == 'test' for (_, key, _) in results), 'limitations': ['Descriptive paired comparison, not a significance test or automatic promotion.', 'Evidence references are recorded, not independently verified by this script.', 'Missing measurements are not measured zero cost.', 'Training frontier is exploratory; validation decisions require held-out evidence.']}


def render(report):
    escaped = html.escape(json.dumps(report, indent=2, allow_nan=False))
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Skill experiment review</title><style>body{font:16px/1.5 system-ui;max-width:1000px;margin:40px auto;padding:0 20px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f4f6;padding:20px}</style><h1>Skill experiment review</h1><p>Recorded evidence only. Eligibility is not proof of improvement or permission to install.</p><pre>'+escaped+'</pre></html>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--json-out', type=Path)
    parser.add_argument('--html-out', type=Path)
    args = parser.parse_args()
    try:
        report = analyze(json.loads(args.input.read_text()))
        for path in (args.json_out, args.html_out):
            if path and path.exists():
                raise ValueError(f'output already exists: {path}; choose a fresh path')
            if path and path.resolve() == args.input.resolve():
                raise ValueError('output must not replace input')
        if args.json_out and args.html_out and args.json_out.resolve() == args.html_out.resolve():
            raise ValueError('JSON and HTML output paths must differ')
        payload = json.dumps(report, indent=2, allow_nan=False)
        if args.json_out:
            with args.json_out.open('x') as f:
                f.write(payload+'\n')
        if args.html_out:
            with args.html_out.open('x') as f:
                f.write(render(report))
        print(payload)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    main()
