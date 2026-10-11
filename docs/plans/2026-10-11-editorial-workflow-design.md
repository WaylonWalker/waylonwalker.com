# Editorial attribution design

Use the existing `authors` field for contributor credit and append versioned
`editorial_history` entries for reviews and edits.  Separate copy editing and
internal link editing so each role has an independent review queue.

An edit has two commits: content and contributor credit first, then a record
linking to that exact commit and file.  This avoids a self-referential SHA.
Records preserve the contributor, importer, timestamp, base revision, result
revision, path, content digest, summary, and GitHub file and diff URLs.

Detect stale reviews by comparing content digests that exclude attribution.
Keep active session state under `.git`, and require clean selected posts.
Commit using an isolated index containing only the session's selected files.
Print all resulting commits.  Existing edits can be imported after ownership
is established and their content commit is created.

A separate ledger would require joining records to posts during ingestion.
Author-only metadata would lose repeated review events and freshness data.
Post-local append-only history supports future markata-go ingestion directly.

The user confirmed that posts with newly added editor credit contain only
that editor's changes.  Import those post diffs as GPT-6 Luna's copy edits;
keep unrelated local changes outside the commits.

The implementation contract and commands live in
[editorial-workflow.md](../editorial-workflow.md).
