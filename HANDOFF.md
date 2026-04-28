# Handoff (initial-build session, 2026-04-28)

> Notes from the session that built this repo. For the next session — whether you're running a mock for the first time, debugging the protocol, or extending the tool.
>
> **Lifecycle: this file is short-lived by design.** It bridges the unrecorded context of the initial-build session. Delete it (or replace with a fresh handoff) once:
> - A real mock has been run end-to-end and its findings folded into `roadmap.md` (top-level), and
> - Design decisions worth preserving have moved into a `CONTRIBUTING.md` or similar.
>
> If you're reading this and the repo already has commit history with real mock-runs, the file is probably stale — verify against the code before trusting any "what's not tested yet" claims here.

## What's in place

- **Mode router** (`CLAUDE.md` at root) — auto-loaded. Defaults to developer mode (normal coding assistant for the tool). Trigger phrase `start mock interview` switches to interviewer mode by loading `INTERVIEWER.md`. Phrase `exit interview` returns to developer mode.
- **Interviewer protocol** (`INTERVIEWER.md` at root) — loaded explicitly via the trigger above. Handles project selection (named or random), permission negotiation, per-feature loop with timing, structured feedback at end. Refuses to edit files while in this mode.
- **One project** (`projects/todo-list/`) — fully specced. Layout is `roadmap.md` (interviewer-only) + `start_folder/` (candidate-facing bundle: README, starter code, tests, first-feature spec). 3 base features (filter / remove / persistence), 2 stretch (tags / undo). Each feature has a `### Spec` block ready to copy and a "what to look for" note for the interviewer.
- **Project contract** (`projects/README.md`) — what files every new project must contain.
- **Feedback rubric** (`feedback_rubric.md`) — 6 dimensions, scoring matrix, common failure patterns. Used by interviewer at end of mock.
- **Meta roadmap** (`roadmap.md` at root) — what to build next for the tool itself: more projects, difficulty self-selection, replay mode, system-design rounds, etc.
- **No bundled pair-programming prompt.** Projects are intentionally tool-agnostic — candidates bring their own AI tool and system prompt (or none). The kit evaluates how the candidate works with AI, not how well a bundled prompt does.

## What's NOT tested yet

- **End-to-end mock has not been run.** The interviewer protocol is plausible but never executed in a real session. First mock will likely surface bugs in:
  - The setup flow (project selection prompt, permission flow)
  - File path inspection (does `ls <path>` work cleanly when the candidate gives `~/...` vs absolute?)
  - The "decide what to drop next" logic during the per-feature loop — needs a real timing test
  - The feedback rubric application — interviewer may need clearer prompts for picking Strong/OK/Weak per dimension
- **No git history yet.** User intends to `git init` themselves before pushing.
- **No CI / linting.** Markdown files only at this point, so probably unnecessary.

## Known caveats / things the next session should watch for

1. **Project selection vs "random" picker** — `CLAUDE.md` says "no need to track history yet, that's a future feature." If the user runs multiple mocks, they'll keep getting `todo-list` (only project). Add `bank-ledger` or another project as soon as possible.

2. **Two-session juggling** — the interviewer is in this repo, the pair programmer is in the candidate's working copy. Both are Claude Code instances. If the candidate uses the same terminal for both, it gets confusing fast. README says "in a separate terminal" but a real user might miss it.

3. **Pair-programmer transcript path** — Resolved. The interviewer reads the JSONL directly (with consent) using the rule: take the candidate's workspace absolute path, replace `/` with `-`, prefix with `~/.claude/projects/`. Documented in `INTERVIEWER.md` Phase 3 and `README.md`. The candidate no longer needs to find or paste anything — only grant read permission.

4. **The interviewer reads `git diff` on the candidate's repo.** Permission is asked, but Claude Code permission prompts may interrupt flow. Worth testing whether `Bash(ls:*, git:*)` should be added to the project's `.claude/settings.json` for smoother execution.

5. **`roadmap.md` (root) is meta** — easy to confuse with `projects/<name>/roadmap.md` (per-project). README and CLAUDE.md both call this out, but if a future contributor moves things around, double-check the references.

## Suggested next steps

In order of value:

1. **Run one full mock end-to-end** on yourself. Use the existing todo-list project. Find every place the protocol breaks. Iterate on `CLAUDE.md` until it's smooth.
2. **Add a second project.** Suggested: `projects/bank-ledger/` (per `roadmap.md`). Prove the project contract works for a different domain.
3. **Add `.claude/settings.json`** with read-only Bash allowlist for the interviewer (so permission prompts don't break flow).
4. **Write `CONTRIBUTING.md`** — how to add a project, what good roadmaps look like. The contract is in `projects/README.md` but more guidance would help external contributors.
5. **License the repo** (probably MIT). Required before public sharing.

## Design decisions worth preserving

- **Two-session split** is deliberate (realism + surprise). Don't collapse to one session "for simplicity".
- **Interviewer never writes code.** This is enforced in `CLAUDE.md` and is part of the realism. If a future maintainer is tempted to make the interviewer "helpful", push back.
- **Honest feedback over soft feedback** is in the rubric. If feedback ever drifts toward "everything was fine!", treat that as a bug.
- **Per-project `roadmap.md` is interviewer-only.** Surprise is core to the experience. Don't move it where the candidate sees it by default.

## Files in this repo and who reads each one

(Mirror of `README.md` for quick reference — if these diverge, README wins.)

| File | Dev mode | Interviewer mode | Candidate |
|------|----------|------------------|-----------|
| `README.md` | informational | informational | yes |
| `CLAUDE.md` (root, mode router) | yes (auto-loaded) | yes (auto-loaded, then routes) | informational only |
| `INTERVIEWER.md` | informational | yes (the protocol) | informational only |
| `roadmap.md` (root, meta) | yes | rarely | informational only |
| `feedback_rubric.md` | yes (when editing) | yes (at end of mock) | optional, post-mock |
| `HANDOFF.md` (this file) | yes | no | rarely |
| `projects/README.md` | yes (when adding projects) | rarely | rarely |
| `projects/<name>/README.md` | yes (when authoring) | yes (project brief: metadata, what's tested, pass/fail anchor) | **NO — interviewer-only** |
| `projects/<name>/roadmap.md` | yes (when authoring) | **yes — interviewer-only** | **NO — keeps surprise** |
| `projects/<name>/NOTE-<DATE>.md` | rarely (gitignored) | **yes — writes during mock, re-reads at feedback time** | **NO — interviewer scratch** |
| `projects/<name>/start_folder/README.md` | yes | yes (for picker description) | yes (copied into their workspace) |
| `projects/<name>/start_folder/<starter>` | yes | yes | yes (copied into their workspace) |

---

Good luck with tomorrow's interview. After it, the most useful thing for this repo would be a real mock-run with notes on what felt smooth and what felt clunky.
