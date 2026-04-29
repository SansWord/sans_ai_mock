# Dev Log — sans_ai_mock

A record of what was built and what was learned, especially around extending the mock-interview framework and running real mock rounds.

## TL;DR

| Version | What shipped |
|---|---|
| [v0.9.3](#v093--readme-disclaimer--ai-audit-recipe-2026-04-28-1716) | Add README "Disclaimer" section noting that `CLAUDE.md` and `.claude/` configs auto-load into Claude Code's context, plus a copy-paste `<details>` recipe for asking a fresh-context Claude Code session (launched from outside the cloned repo) to audit configs before running anything; drop two stale CLAUDE.md bullets that described `NOTE-2026-04-28.md` as a "committed example exception" (it was always gitignored) |
| [v0.9.2](#v092--trigger-phrase-standardization--interviewer-bash-allowlist-2026-04-28-1632) | Standardize the mock-interview trigger phrase to a single canonical `start mock interview` (drop the dual "first-time" wording); add `.claude/settings.json` with a tight read-only Bash allowlist (`ls`, `git status,diff,log,show`, `cat`, `date`, `wc`, `jq`) so per-feature inspection no longer prompts |
| [v0.9.1](#v091--devlog--claudemd-conventions-2026-04-28-1621) | Set up `docs/devlog.md` with TL;DR + learning-tags table; add documentation list, versioning rule, end-of-session reminder, tailored "ship it" shortcut, and GitHub upload safety section to CLAUDE.md |
| [v0.9.0](#v090--first-end-to-end-mock--comprehensive-post-mortem-fixes-2026-04-28-1615) | Battle-tested with first 60-min mock; folded findings into protocol/rubric/projects; new "Spec-as-starting-point" pattern; seniority calibration; container/plug-in architecture documented; HANDOFF.md retired and absorbed into CLAUDE.md |
| [v0.0.0](#v000--initial-build--pre-mock-iteration-2026-04-28) | Initial build of the framework: mode router, INTERVIEWER.md protocol, todo-list project (3 base + 2 stretch features), feedback rubric, project contract, top-level meta-roadmap |

---

### Learning tags

| Tag | Meaning |
|-----|---------|
| `[note]` | Useful context, well-documented — good to have written down but you'd find it in the docs |
| `[insight]` | Non-obvious; meaningfully changes how you design or debug something |
| `[gotcha]` | A specific trap that bit you; high risk of biting you again — bookmark this |

---

## v0.9.3 — README disclaimer + AI-audit recipe (2026-04-28 17:16)

**Review:** not yet

**What was built:**
- **README "Disclaimer" section** — explicit notice that `CLAUDE.md` and `.claude/` configs in any repo auto-load into Claude Code's context (their instructions become part of how the agent behaves), with a directive to read `CLAUDE.md`, `INTERVIEWER.md`, and any other auto-loaded files before running someone else's repo. Generalizes to "review unfamiliar code, scripts, or AI prompts before running them."
- **`<details>` "How to ask Claude Code to audit this repo safely" block** — copy-paste recipe: launch `claude` from a folder *outside* the cloned repo (so the repo's own configs don't auto-load), then point that session at the repo path with a prompt that asks for a read-only audit covering hooks/auto-run shell, exfiltration vectors, prompt-injection content, and unexpected file writes. Because the auditing session has no auto-loaded instructions from the audited repo, its review is independent.
- **CLAUDE.md "GitHub Upload Safety" cleanup** — removed two bullets that described `projects/todo-list/NOTE-2026-04-28.md` as a "committed example exception." The file was never committed (matched by the existing `.gitignore` rule `projects/*/NOTE-*.md`). Bullets now keep only the general guidance: don't stage NOTE files, use placeholder paths in examples.

**Key technical learnings:**
- `[insight]` Auto-loaded agent configs are a real-but-quiet supply-chain surface. `CLAUDE.md` and `.claude/settings.json` (and any `.claude/hooks/*` if present) shape an agent's behavior the moment a session opens in that folder — invisibly to anyone who hasn't read them. Putting a disclaimer at the top of the README, plus a concrete "how to audit" recipe, treats this honestly instead of hand-waving "trust the repo."
- `[insight]` The "audit from outside the cloned repo" pattern is the key trick. A subagent dispatched while `cwd` is the audited repo would still inherit the very `CLAUDE.md` we want to audit. Launching from `~` (or any other folder) and pointing the session at the path keeps the auditor's context clean.

**Process learnings:**
- `[gotcha]` Eating our own dog food: ran the recipe with a fresh-context subagent against this repo before shipping. Verdict came back SAFE WITH NOTES — but it confidently described `NOTE-2026-04-28.md` as a "committed example" when it was always gitignored and untracked. The auditor was faithfully repeating a stale claim from CLAUDE.md, not checking `git ls-files`. Lesson: AI audits read docs as ground truth; cross-check any "X is committed / X is shipped" claim against `git ls-files` / `git log` before acting. The audit caught no real risk but did surface this doc-vs-reality drift, which is exactly the kind of thing the disclaimer ecosystem is supposed to surface.
- `[note]` Patch versions are the right home for doc/safety polish — no behavior change, no new feature, just clearer + more honest framing.

---

## v0.9.2 — trigger-phrase standardization + interviewer Bash allowlist (2026-04-28 16:32)

**Review:** not yet

**What was built:**
- **Standardized the mock-interview trigger to a single canonical phrase: `start mock interview`.** The README previously documented a dual form (`help me setup and start mock interview` for first-timers, `start mock interview` for repeat users). The dual form added zero functional value — the protocol's Phase 1 walks every candidate through full setup regardless — and it implied a behavioral difference that didn't exist. README "Kickstart prompts" and "Quick start" sections now both use the bare canonical phrase, with explicit copy noting that the full setup walkthrough runs every time.
- **`.claude/settings.json`** — first checked-in settings file for this repo. Read-only Bash allowlist for the commands the interviewer protocol invokes during a mock: `ls`, `/bin/ls`, `git status`, `git diff`, `git log`, `git show`, `cat`, `date`, `wc`, `jq`. Pre-approves the per-feature inspection flow (Phase 2 step 3a) and the JSONL transcript flow (Phase 3 step 2) without granting any write/destructive permissions.
- **Deliberately NOT auto-allowed:** `python3 -m pytest` / `python3 test_*.py` / `pytest` (running candidate test code is a different threat surface — should still prompt). `Read(~/.claude/projects/**)` (transcript-dir read scope; per-session consent stays in place). `cp` / `mv` / `rm` / `mkdir` / `git add` / `git commit` / etc. (all write/state-mutating commands intentionally excluded).
- **`roadmap.md`** — backlog item for `.claude/settings.json` crossed off with strikethrough + `(v0.9.2)` tag, including a parenthetical noting which commands shipped and which were deliberately excluded. Sets the convention for how future shipped backlog items get marked.

**Key technical learnings:**
- `[insight]` Auto-allowing read-only Bash commands removes real friction during a mock without changing the security posture meaningfully — the same commands would be approved every round anyway. The interesting line is *between* read-only inspection (always-allow) and code execution (still prompt). Putting `python3 -m pytest` on the prompt side keeps a meaningful checkpoint: the interviewer reads code freely, but executing arbitrary candidate code stays a deliberate consent moment.
- `[note]` Trigger-phrase standardization is one of those quiet wins where the change is small but the prior dual-form was actively confusing: a first-time user reading the README would think "do I need the prefix?" and a returning user would wonder if they were missing setup. One canonical phrase + an explicit "setup runs every time" line removes both confusions.

**Process learnings:**
- `[note]` First "ship it" run after defining the shortcut in v0.9.1 — the flow worked clean: stage → devlog → commit → tag → verify, no improvisation needed. The convention will hold up as long as version-naming decisions stay simple (patch vs. minor); the moment a release decision needs more thought, the user gets to call it.

---

## v0.9.1 — devlog + CLAUDE.md conventions (2026-04-28 16:21)

**Review:** not yet

**What was built:**
- `docs/devlog.md` initialized with TL;DR table, learning-tags reference table, full v0.9.0 entry, retroactive v0.0.0 entry, and this v0.9.1 self-entry.
- CLAUDE.md gained five sections: a `Documentation (docs/)` index that lists every `docs/*.md` file with a one-liner; a project-local `Versioning` section restating the three-part semver rule; an `End of Session` reminder; a sans_ai_mock-tailored `"Ship it" shortcut`; and a `GitHub Upload Safety` section.
- The "Ship it" shortcut is intentionally lighter than `sans_cube`'s template: this repo has no test suite, no build step, and no feature-branch convention yet, so the flow is `stage → devlog → tag → commit`. Future build-out (multi-project automation, CI checks) will extend it.

**Process learnings:**
- `[note]` First time using the "ship it" shortcut on this repo; v0.9.1 is itself the release that defines the flow. Reasonable bootstrap pattern: define the convention, then immediately apply it.
- `[note]` Mirroring `sans_cube`'s docs conventions intentionally — keeping the format consistent across SansWord's repos so devlog reading and version comparisons work the same way everywhere.

---

## v0.9.0 — first end-to-end mock + comprehensive post-mortem fixes (2026-04-28 16:15)

**Review:** complete (two subagent consistency reviews + one manual cross-check)

**What was built:**
- **First end-to-end mock run** of the framework. 60-minute todo-list session: candidate completed F1 (filter) and F2 (remove), ran out of time on F3 (persistence) due to scope creep on F1 (added `status` field on `Todo` despite explicit "out of scope: status enums" line).
- **New "Spec-as-starting-point" anti-pattern** added to `feedback_rubric.md` — captures the failure mode the first mock surfaced: excellent process discipline (spec, plan, TDD, push-back) applied to a scope larger than the given spec. Distinguishing tell: artifacts look strong in isolation but the diff exceeds minimum-viable. Yellow at junior, red at senior.
- **Seniority calibration** now asked at Phase 1 step 1 (`junior IC1–IC2 / mid IC3–IC4 / senior IC5+ / uncalibrated`). Drives pattern-level flag colors at feedback time. Saved into NOTE Setup section and surfaced in the candidate-facing feedback file.
- **Container/plug-in architecture** documented in `CLAUDE.md`: framework layer (interviewer protocol, rubric, root docs, `projects/README.md` contract) vs project layer (`projects/<name>/`). Strict dependency rule: project depends on framework, never reverse. Five concrete implications enumerated.
- **Phase 1 setup overhaul**: hand candidate literal `cp` + `git init` commands instead of natural-language description; bundle workspace + JSONL permissions up-front (was: JSONL asked mid-feedback under pressure); explicit reply formats (`yes both` / `yes 1, no 2` / etc.); clarify clock semantics (60-min coding clock; feedback is *post-clock and untimed*).
- **Phase 2 additions**: mandatory scope probes added to probing-question list; clarification-question decision tree (`answer directly` / `punt back` / `"what does spec say?"`); single-feature overrun decision tree (≥2× budget) with scripted A/B prompt.
- **Phase 3**: drop redundant in-line JSONL ask; document underscore-to-hyphen path-encoding rule explicitly (with `/bin/ls -1t` for the macOS BSD `ls` gotcha).
- **NOTE template**: per-feature `Ended:` line now captures `actual <X> min vs. <Y> min target → <Z>×`; `Permission` field split into `(workspace read)` + `(JSONL transcript)` flags; `Target seniority` line added; `Time discipline` line in Round summary.
- **Feedback file template** restructured: action items moved above What-went-well (so they're the first thing the candidate sees on re-read); "How to use this file" header added; `Features attempted but not finished` row.
- **Separation of concerns**: `projects/todo-list/README.md` rewritten as a question spec (domain + rubric-dimension exposure map + where-to-look). Removed: round length, target seniority, target role, when-to-pick, pass/fail anchor — all relocated to framework concerns.
- **F1 spec verbatim-synced** between `start_folder/todo_feature.md` and `roadmap.md` (with note flagging the dual-bundling). Out-of-scope bullets promoted from list to named contract; Acceptance #4 added: minimum-viable diff as a testable acceptance criterion.
- **HANDOFF.md retired**. Architecture principles + design decisions + cross-mode file table absorbed into CLAUDE.md; settings.json TODO migrated to roadmap.md backlog.
- **Misc**: python3 standardization in candidate-facing test commands; redundant copy/git-init instructions stripped from `start_folder/README.md` (the interviewer now provides them).

**Key technical learnings:**
- `[insight]` "Spec-as-starting-point" is a failure mode the original rubric's named patterns ("Trust the AI", "Bypass discipline", etc.) didn't cover. The candidate's discipline was excellent in isolation; the gap was scope. Naming the pattern matters because it's invisible to autopilot probing — the artifacts and process all look right. Only direct scope-tracing surfaces it. The mandatory scope probe in Phase 2 step 3b is the operational fix.
- `[insight]` Container + plug-in architectures need their dependency rule stated *and* spot-checked. Writing "project depends on framework, never the reverse" in CLAUDE.md isn't enough — you have to actually grep `INTERVIEWER.md` and `feedback_rubric.md` for project-name leakage. Spot-check passed (no leaks except a deliberate exemplar reference at `CLAUDE.md:96` to `projects/todo-list/` as the "see how it's done" pointer).
- `[insight]` Asking permission *up-front* and bundling related permissions changes the candidate's experience materially. The original protocol asked workspace permission in Phase 1 and JSONL permission mid-feedback (Phase 3 step 2). The latter created a coercive yes/no when the candidate was about to receive feedback. Bundling fixes both the friction and the implicit pressure.
- `[gotcha]` Restructuring a doc creates broken cross-references in OTHER docs that describe its old contents. Two consistency-review batches caught these:
  - `projects/README.md`'s contract description still listed "metadata, target seniority, when-to-pick, pass/fail anchor" after I restructured `projects/todo-list/README.md` to remove those.
  - `README.md`'s "Files the candidate should NOT peek at" entry described the project README's old contents.
  - `HANDOFF.md`'s file-roles table — fixed transitively when HANDOFF was deleted.
  Lesson: after any doc restructure, grep for prose descriptions of the changed file's contents.
- `[gotcha]` When a markdown code block (e.g. the workflow-reminder block shown to the candidate) interrupts a numbered list in the protocol, the next item silently keeps the same number. Pre-restructure, Phase 1 had two step 6's (Brief + Start the clock) and a cross-reference to "Phase 1 step 6 (Start the clock)" pointing at the wrong target. Caught only in the second consistency review. Lesson: numbered lists with embedded code blocks need explicit number checks after any insertion.

**Process learnings:**
- `[insight]` Two consecutive consistency-review subagent calls were both useful and non-overlapping. Round 1 caught structural mismatches (timing claims, F1 spec drift, NOTE template inconsistency). Round 2 caught narrower drift introduced *by* the round-1 fixes (vocabulary mismatch in the new seniority data flow, leftover stale descriptions of removed sections). The cost of an extra review pass is much lower than the cost of finding these in production use.
- `[insight]` "Telegraph what you measure, don't hide it" was the right call for the candidate-facing workflow reminder. Items 5–7 (push-back, edge-case ownership, scope discipline) are explicitly framed as "habits I'm measuring" with a note that real interviews won't pre-disclose. Practice value over assessment-purity.
- `[note]` HANDOFF.md was load-bearing for ~one mock cycle, then became dead weight. Triaging its sections (architecture principles → CLAUDE.md, file-roles table → CLAUDE.md, settings.json TODO → roadmap.md, everything else → delete) was straightforward once the criterion ("does this still describe current state?") was applied per-section.

---

## v0.0.0 — initial build + pre-mock iteration (2026-04-28)

**Review:** retroactive snapshot

**What was built:**
- Initial framework: `CLAUDE.md` mode router (developer mode default; `start mock interview` triggers interview mode by loading `INTERVIEWER.md`; `exit interview` returns).
- `INTERVIEWER.md` — three-phase protocol (Setup, per-feature loop, wrap-up + feedback). Permission negotiation, NOTE-file format for durable observations across context compaction, JSONL transcript reading for Claude Code candidates.
- `feedback_rubric.md` — six dimensions (spec discipline, prompt quality, push-back, test discipline, edge-case awareness, verification & ownership), Strong/OK/Weak scoring matrix, common anti-patterns.
- `projects/todo-list/` — first project: 3 base features (filter / remove / persistence) + 2 stretch (tags / undo). `start_folder/` candidate-facing bundle, `roadmap.md` interviewer-only feature list.
- `projects/README.md` — contract for adding new projects.
- Top-level `roadmap.md` — meta-roadmap for extending the kit (additional projects, candidate UX, feedback improvements, different round formats).
- `HANDOFF.md` — initial-build session notes (later retired in v0.9.0).
- Pre-v0.9.0 iteration commit (`83c425b`, "after first round, subagent review transcript and purpose these changes") — first round of subagent-driven review changes; specific contents not separately devlogged here, see commit diff.

**Process learnings:**
- `[note]` Retroactive entry — the framework existed and was iterated on before the first end-to-end mock validated it. v0.9.0 is the first version battle-tested in a real round.
