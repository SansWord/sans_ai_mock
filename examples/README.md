# Examples

Anonymized artifacts from real mock-interview runs — useful as a preview of what to expect, and what "honest feedback" actually looks like, before you commit a 60-min round of your own.

## Runs

- [`2026-04-28-todo-list/`](2026-04-28-todo-list/) — first round on the `todo-list` project. Borderline outcome: strong process discipline, but F1 scope-creep cost F3. Includes the candidate's spec/plan files, the final code, and the end-of-mock feedback.

## What you get from reading these

- **A concrete preview of feedback.** The rubric in `feedback_rubric.md` describes what gets assessed; the example feedback file shows what an actual assessment reads like. If you've ever wondered whether "honest feedback" means a soft pat on the back or an actual list of failure modes, this answers it.
- **A read on the spec → plan → test → impl loop.** Each example folder includes the spec and plan files the candidate wrote, alongside the feedback's commentary on them. Useful for seeing where the workflow paid off and where it leaked.
- **A baseline for "how much should I ship in 60 min?"** — useful both for candidates calibrating against the pass anchor, and for anyone evaluating whether this kit produces realistic round volume.

## How feedback files are produced

After the 60-min coding window ends, the interviewer runs Phase 3 of `INTERVIEWER.md`: synthesizes observations from the running NOTE-file, applies the 6-dimension rubric in `feedback_rubric.md`, and writes a markdown file to the candidate's workspace named `feedback-<YYYY-MM-DD>-<project>.md`. Each example here is one such output, lightly redacted for publication (private paths removed; first-person phrasing kept since it reflects how real feedback reads).

## Caveat

These are **single data points**, not benchmarks. One candidate, one round each. Read them as "here's what one mock looked like," not "here's what every mock should look like."
