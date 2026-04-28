# Tool Roadmap (meta — for the mock interview tool itself)

> This is the roadmap for **extending the mock-interview tool**, not for any single project a candidate works on. (For the per-project feature lists used inside a mock, see `projects/<project-name>/roadmap.md`.)
>
> If you're cloning this repo to use it for practice, you don't need to read this file. It's for contributors / future-me.

## Vision

A reusable, self-contained mock-interview kit for the AI-pair-programming round. Anyone can clone the repo, run `claude` in it, say "start mock interview", and get a structured 1-hour mock with honest feedback. Multiple project domains, multiple difficulty levels, single tool.

## Status (initial release)

- [x] Single project (`projects/todo-list/`) with 3 base + 2 stretch features
- [x] Two-session architecture (interviewer in repo, pair programmer in candidate's working dir)
- [x] Six-dimension feedback rubric
- [x] Setup phase with permission negotiation + working-directory inspection
- [x] Time tracking + pacing logic for "what to drop next"

## Near-term — additional projects

Each new project must follow the contract in `projects/README.md`. Suggested next:

- [ ] **`projects/url-shortener/`** — Flask/FastAPI POST /shorten + GET /:code, follow-ups for TTL / analytics / custom aliases
- [ ] **`projects/bank-ledger/`** — `Account.deposit/withdraw`, follow-ups for transfer / overdraft / interest accrual
- [ ] **`projects/pomodoro-cli/`** — start/stop/pause/log, follow-ups for stats / configurable durations / multi-task tracking
- [ ] **`projects/markdown-to-slides/`** — parse markdown, split by `---`, render to HTML; follow-ups for themes / speaker notes / export to PDF

The point is **domain variety**: a candidate using this tool for repeated practice shouldn't see the same domain twice in a row.

## Near-term — better candidate UX

- [ ] **Random project picker.** Candidate can say "start a random mock" and the interviewer picks a project they haven't seen recently (track via session log).
- [ ] **Difficulty self-selection.** "I want a senior-level mock" vs "junior-level mock" — interviewer adjusts time targets, feature complexity, and feedback bar.
- [ ] **Domain self-selection.** "I want to practice REST APIs" → interviewer offers projects tagged `rest`. Tag taxonomy lives in each project's README front matter.
- [ ] **Replay mode.** "I bombed feature 3, can we restart from there?" — interviewer accepts a replay request and re-drops the same spec without resetting timing.

## Near-term — better feedback

- [ ] **Reference implementations** per project, per feature. After the mock, candidate can read how a strong candidate would have solved it. Stored at `projects/<name>/reference/feature-<n>.md`.
- [ ] **Common failure patterns** doc per project: what 80% of candidates miss on this feature, so feedback can tag failure modes.
- [ ] **Transcript analysis.** Interviewer parses the pair-programmer JSONL automatically (counts prompts, identifies one-shot accepts vs. push-back patterns) and quotes specific moments in feedback.

## Mid-term — different round formats

- [ ] **System design round.** Different protocol entirely — no code, just diagrams and tradeoffs. Different rubric.
- [ ] **Debugging round.** Interviewer drops a buggy codebase, candidate reproduces and fixes. Tests AI-pairing under "find the root cause" pressure.
- [ ] **Code review round.** Interviewer drops a diff, candidate reviews it (with AI assistance). Tests "evaluate someone else's code" muscle.

## Mid-term — multi-language support

- [ ] Add `language: python` to each project's README front matter. Allow `projects/url-shortener-go/` etc.

## Long-term — community

- [ ] **`CONTRIBUTING.md`** — how to add a project, what the contract is, what good roadmaps look like.
- [ ] **Examples folder** — sample completed mocks (with anonymized transcripts and feedback) so people can see what good practice looks like before doing their own.
- [ ] **LICENSE.** Probably MIT to keep it permissive.

## Backlog from cold-read review (2026-04-28)

Items surfaced by a fresh-context audit of the docs. The high-priority items (Phase 1 missing tool question, pass-anchor / time-table mismatch, Feature 2+ delivery contradiction, decline-permission fallback, path-encoding rule, rubric Dim 4/5 overlap) have been fixed. These are the rest:

- [ ] **`HANDOFF.md:35` says "Both are Claude Code instances."** Counter to the tool-agnostic pivot — pair-programmer side can be any tool. Update.
- [ ] **`README.md:60` "Two Claude (or compatible) sessions."** Claude-first framing. Replace with explicit asymmetry: interviewer side requires Claude Code (mode-router lives in `CLAUDE.md`), candidate side is tool-agnostic.
- [ ] **`start_folder/README.md` still names `feature.spec.md` / `feature.plan.md`.** Claude-Code/Superpowers convention leaking into candidate-facing instructions. Either soften to "an example workflow" or strip.
- [ ] **Picker-description spec says "first paragraph"** which is fuzzy and easy to overload. Tighten contract in `projects/README.md` to "first sentence" or a hard char limit.
- [ ] **Run one full mock end-to-end on yourself.** Still unrun. Fold findings back into protocol + retire `HANDOFF.md` once findings are absorbed.
- [ ] **HANDOFF.md lifecycle.** Currently doing double duty (initial-build artifact + ongoing notes). Decide: delete after first real mock per its stated lifecycle, OR rename to a durable doc (e.g. `CONTRIBUTING.md` / `NOTES.md`).
- [ ] **`feedback_rubric.md` headings with `&`** produce ugly auto-anchors (`#1-spec--plan-discipline`). Cosmetic — fix if anyone starts linking to dimensions.
- [ ] **No `.gitignore` in `start_folder/`.** When the candidate runs `git init && git add .`, they pick up `__pycache__/` after first test run. Minor mock friction.
- [ ] **Time budget not stated to candidate.** Interviewer knows 60 min; candidate sees vague "time pressure." Consider stating the round length in the candidate-facing workflow reminder.
- [ ] **Verify access tilde-expansion edge case.** `INTERVIEWER.md` `ls <path>` step doesn't tell the interviewer to expand `~` first. Usually works but can fail if path is passed quoted. Defensive note.
- [ ] **Documentation drift surface.** "Files the candidate should not peek at" exists in 4 places (root README, INTERVIEWER.md, projects/README.md, HANDOFF.md). Pick one canonical source and have others link to it.
- [ ] **Project-layout diagrams duplicated** (root README, projects/README.md ×2). Same drift risk.
- [ ] **Calibrate the rubric and pass anchor** against real data. Both were authored from reasoning, not observation. Once a few mocks have run, revisit which dimensions actually distinguish strong from weak candidates.

## Non-goals

- **Replacing real interviews.** This is for practice. Real interviewers see your screen, your face, your timing — a Claude session can only approximate.
- **Grading rigor.** Feedback is qualitative and honest, not standardized. We don't try to give a numeric score that's comparable across candidates.
- **Hiring decisions.** Don't use this to filter candidates. It's for self-improvement.

## How to contribute (TODO: flesh out in CONTRIBUTING.md)

1. Pick a `[ ]` item above (or propose your own).
2. If it's a new project, read `projects/README.md` for the contract.
3. Open a PR with the addition. Include at least one full mock walkthrough you ran on the new project to validate.
