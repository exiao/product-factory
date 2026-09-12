# Typefully platform and comment rules

Use platform names supported by the current CLI (`x`, `linkedin`, `threads`, `bluesky`, `mastodon`) and verify the connected social set before creating content. A LinkedIn organization mention uses resolver output such as `@[Company](urn:li:organization:<ID>)`; do not guess the URN.

Draft comments are represented by inline `<typ:comment-thread>` anchors. When editing a draft, preserve each anchor and move it with the selected text or paragraph it annotates. Never resolve or delete a thread merely because the text appears addressed; that requires explicit instruction.

Use Typefully's own scratchpad option for notes attached to a draft. Do not confuse local files with Typefully draft notes. Check publishing quota through `social-sets:get` before scheduling a large batch, and surface quota failures rather than retrying blindly.
