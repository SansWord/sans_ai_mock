# Dev Log — sans_ai_mock

A record of what was built and what was learned, especially around extending the mock-interview framework and running real mock rounds.

## TL;DR

| Version | What shipped |
|---|---|
| [v0.9.7](#v097--promote-example-to-own-section--subscription-tier-cost-framing-2026-04-29-0038) | Promote the example link from a parenthetical inside "How it works" to its own `## Real run example` section between How-it-works and Quick start (better for skim-readers; the example was a top-2 senior-eng-review blocker); reframe cost guidance for subscription users — replace the API-dollar headline with a Pro / Max 5x / Max 20x fit table (Pro tight, Max 5x comfortable, Max 20x plenty of room), keeping raw API as a fallback line for those running on direct API; mirror the same subscription-tier breakdown into the example folder's cost section |
| [v0.9.6](#v096--first-example-folder--note-file-rationale--cost-numbers-2026-04-28-1756) | Ship the first end-to-end example under `examples/2026-04-28-todo-list/` (candidate's spec/plan files for both features, final code, end-of-mock feedback, per-folder README explaining read order + outcome + measured API cost); add a new "Why the interviewer writes a NOTE file" README section covering durable-memory + candidate-review rationale; measure the 2026-04-28 mock's actual token usage by parsing both interviewer and candidate JSONL transcripts (deduped by `message.id`) and publish the numbers (~$19 for the 60-min coding window, ~$26 for the full experience on Opus 4.7); link the example from the README's How-it-works callout, repo-structure tree, and Problem List; partial-complete the `Examples folder` roadmap backlog item |
| [v0.9.5](#v095--readme-senior-eng-review-pass-2026-04-28-1736) | First-30-seconds README pass driven by a senior-eng review: add an upfront "60-minute round + Claude Code on interviewer side, anything on candidate side" meta-info line; collapse the redundant "Kickstart prompts" section into the existing Quick start; compress "Repo structure" to a 5-line skeleton (full annotated tree moved to `CONTRIBUTING.md`); shrink the visible Disclaimer prose to a single sentence (audit recipe still in `<details>`); tighten the JSONL-transcript bullet (drop path-encoding mechanics); reframe Status to be honest about what ships today vs the roadmap; fix the lingering "Two Claude (or compatible) sessions" Claude-first framing in How-it-works |
| [v0.9.4](#v094--contributingmd-split--readme-tightening-2026-04-28-1730) | Move developer-mode kickstart prompts and contributor guidance out of README into a new `CONTRIBUTING.md` at repo root (mode awareness, repo orientation, common tasks, conventions, PR guidance); README "Kickstart prompts" loses the dev-mode subsection in favor of a one-line pointer; "Contributing" section becomes a pointer; "About" → "About Author" with the `**Author:**` prefix dropped; clone command uses the real GitHub URL; closes the `CONTRIBUTING.md` backlog item from `roadmap.md` |
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

## v0.9.7 — promote example to own section + subscription-tier cost framing (2026-04-29 00:38)

**Review:** not yet

**What was built:**
- **Promoted the example link to its own `## Real run example` section.** Previously a parenthetical sentence inside "How it works"; now a top-level section between How-it-works and Quick start so it shows up in GitHub's auto-generated TOC and on first scroll. The senior-eng review explicitly flagged "no preview of what 'honest feedback' looks like" as one of the two top blockers — making the example more discoverable directly addresses that.
- **Reframed cost guidance for subscription users.** Previous version led with "~$19 in API usage" — accurate but not what most readers actually pay. Replaced with a per-plan fit table:
  - Claude Pro: tight (likely hits the 5h rolling window mid-mock)
  - Claude Max 5x: comfortable (~1 mock per 5h window with headroom)
  - Claude Max 20x: plenty of room (multiple mocks per 5h window)
  - Raw API: ~$19 / ~$26 retained as a fallback line for direct-API users
- **Mirrored the subscription tiering into `examples/2026-04-28-todo-list/README.md`** — the existing "Claude Code subscription vs raw API" bullet got expanded with sub-bullets for Pro / Max 5x / Max 20x. Headline number and detail breakdown now agree.
- Section ordering after this release: header → Disclaimer → How it works → **Real run example** (new) → Quick start → Repo structure → Why two sessions → Why the interviewer writes a NOTE file → Files the candidate should NOT peek at → Tips → Contributing → Problem List → About Author. The mechanics-then-preview-then-action flow is now visible without scrolling past redundant content.

**Key technical learnings:**
- `[insight]` "How much does it cost?" answered in dollars is mostly noise for the subscription audience that drives Claude Code adoption. The right unit for those readers is **fit-against-quota** ("comfortable on Max 5x") not absolute price ("~$19"). Keeping the dollar number as a fallback line for raw-API users covers both audiences without leading with the wrong frame for the majority.
- `[note]` Anthropic does not publish exact 5h-window quotas and adjusts them periodically — so the right framing is qualitative tiers ("tight / comfortable / plenty of room") rather than precise percentages, which would invite "actually it's 47%, not 50%" pushback that's not the point.

**Process learnings:**
- `[insight]` Trust signals from a one-line sentence inside an existing section ≠ trust signals from a `##` heading at the same depth as Disclaimer / Quick start / Why two sessions. The same content gets very different visibility based on heading level. When something is the answer to a top blocker, give it the heading. When it's supporting detail, keep it inline.

---

## v0.9.6 — first example folder + NOTE-file rationale + cost numbers (2026-04-28 17:56)

**Review:** not yet

**What was built:**
- **First end-to-end example** at `examples/2026-04-28-todo-list/` — drawn from the real 2026-04-28 mock that produced the v0.9.0 post-mortem. Includes the candidate's `001-status-field.{spec,plan}.md`, `002-remove-todo.{spec,plan}.md`, the final `todo.py` + `test_todo.py`, and `feedback.md` (the end-of-mock feedback file). Plus a per-run `README.md` that frames outcome, read order, and the measured cost. Lightly redacted: only the feedback's "your project CLAUDE.md" reference was edited to disambiguate from the framework's `CLAUDE.md`.
- **`examples/README.md`** parent index — explains what examples are for, lists the runs available, and notes the single-data-point caveat.
- **New "Why the interviewer writes a NOTE file" README section** — explicit two-purpose rationale: (1) durable memory across context compaction during a 60-min mock, (2) candidate-review artifact post-mock. Placed right after "Why two sessions" to cluster design-rationale content.
- **Cost measurement** — parsed both interviewer-side (`~/.claude/projects/-Users-sansword-Source-github-sans-ai-mock/1fc13251-...jsonl`) and candidate-side (`~/.claude/projects/-Users-sansword-Source-ai-coding-first-round/630fa990-...jsonl`) JSONL transcripts with `jq`, deduped by `message.id`, broken out by model. Result: ~$2.79 interviewer + ~$16.36 candidate = ~$19.15 for the 60-min coding window; ~$26.14 for the full experience including setup + Phase 3 feedback delivery. Published the breakdown in the example folder's `README.md` and a one-line callout in the main README's How-it-works section.
- **README repo-structure tree** — added `examples/` row.
- **`CLAUDE.md` orientation table** — added a row for `examples/<run>/` (writeable in dev mode; rarely-read in interview mode because past feedback could prime live judgments; readable by candidates as preview / post-mock reference).
- **`CONTRIBUTING.md` framework-layer list** — added `examples/README.md` pointer.
- **`roadmap.md`** — `Examples folder` backlog item marked partial-complete with `(v0.9.6 — ...)` parenthetical noting the first example shipped and what's still pending (pair-programmer transcripts, additional runs).

**Key technical learnings:**
- `[insight]` Cache reads dominate the bill (~50% of cost on this run). Without prompt caching the same usage would have cost ~10x more on the cache_read path. The architecture-level decision to put long-lived files (CLAUDE.md, INTERVIEWER.md, project README, roadmap) into the auto-load context isn't free, but with caching the marginal cost-per-turn collapses by an order of magnitude. Worth knowing when designing protocol surface.
- `[insight]` Senior-eng "is it $0.50 or $15?" hypothesis was off by ~2x in the more-expensive direction. The honest answer is "~$19 for the live coding window, ~$26 for the full experience" — closer to a coffee-and-lunch than a cheap experiment. Worth showing candidates upfront so they don't bounce on first surprise charge, and worth honest-framing for hiring managers evaluating the kit for team use.
- `[gotcha]` Claude Code JSONL transcripts have **multiple records per assistant turn** (different `.timestamp` but identical `.message.id` and identical `.message.usage`). Naively summing usage across all records double-counts by ~3x. Always dedupe by `message.id` before summing tokens. The `iterations` field inside `usage` is not a separate cost surface; it's a per-thinking-step breakdown of the same total.
- `[note]` `cache_creation_input_tokens` splits into `ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens` (1h cache writes are 2x the input price; 5m writes are 1.25x). On this run all cache writes were 1h — Claude Code currently uses 1h ephemeral caching by default for system context.
- `[insight]` The senior-eng review specifically called out "no preview of what 'honest feedback' looks like" as one of two top blockers. Shipping the example folder addresses it concretely — the feedback file is publicly verifiable evidence that the rubric isn't vague. The cost section addresses the other half of the trust gap ("what does this actually cost me to try?").

**Process learnings:**
- `[note]` The flow for this release was driven by reviewer feedback (the senior-eng subagent run identified the gaps), then user-iterated (each new piece — example folder, NOTE-file rationale, cost numbers — was a separate user message). Patching incrementally rather than batching let each piece get scoped and shipped without scope-creep on the rest. The four-patch run (v0.9.3 → v0.9.6) all polished the public surface for LinkedIn promotion.
- `[note]` Re-using the actual transcripts of the v0.9.0 mock to build the example folder means the artifacts are 100% authentic — no synthesized "looks like a mock" filler. The downside (single data point, single candidate, candidate is the author) is worth flagging in the example README and taking on as a future "more runs" backlog item.

---

## v0.9.5 — README senior-eng review pass (2026-04-28 17:36)

**Review:** not yet

**What was built:**
- **Upfront meta-info line** — directly under the opening tagline: *"60-minute round. You need Claude Code on the interviewer side; on the candidate side, use any AI tool (Claude Code, Cursor, Copilot CLI, Gemini CLI) or none."* Answers the two "first 30 seconds" questions a senior-eng reader has (time budget + tool requirements) without making them scroll.
- **Collapsed redundant Kickstart-prompts section** — the README previously had a "Kickstart prompts > To run a mock" section that was a teaser version of the Quick start walkthrough below it. Removed the entire section; Quick start is now the canonical "how to run." The dev-mode pointer to `CONTRIBUTING.md` lives in the bottom Contributing section, so no info was lost.
- **Compressed Repo structure** — went from a ~21-line annotated tree to a 5-line skeleton showing only top-level files + `projects/<name>/`. Detailed per-file annotation (interviewer-facing brief, hidden roadmap, NOTE scratch, candidate-facing bundle) moved to `CONTRIBUTING.md` "Project layer" section, where it's actually useful (contributors adding a project).
- **Disclaimer shrunk to one sentence** — the visible prose collapsed from ~3 lines + a follow-up paragraph to a single sentence; the `<details>` audit recipe is unchanged. Less of a speed-bump for readers landing from LinkedIn who just want to try a mock.
- **JSONL transcript bullet tightened** — dropped the path-encoding mechanics (workspace `/Users/you/scratch` → `~/.claude/projects/-Users-you-scratch/` etc.). The implementation belongs in `INTERVIEWER.md`; the README only needs the *what* (interviewer can quote your prompts) and *why* (deeper feedback). 6 lines → 3.
- **Status section reframed** — was "Initial release. One project (todo-list)." which contradicted the (now-removed) opening "Multiple project domains" claim. Now: *"Ships with the todo-list project (Python). Roadmap targets bank-ledger, url-shortener, pomodoro-cli, and others."* Honest about today's scope while pointing at the trajectory.
- **Fixed Claude-first "How it works" framing** — "Two Claude (or compatible) sessions" → "Two sessions run in parallel — the interviewer side runs in Claude Code; the candidate side is tool-agnostic." Closes the longstanding backlog item from v0.9.0 review.

**Key technical learnings:**
- `[insight]` Senior-eng readers are looking for **time budget and tool requirements within the first scroll**. Burying those in a tip block at line 156 (where the JSONL transcript bullet was) costs you readers who would otherwise have tried the tool. Putting the meta-info line right under the tagline is high-leverage real estate.
- `[insight]` "Multiple project domains" sounds like a feature claim but is actually a roadmap promise when only one project ships. The right move on a single-project release is to **lead with what you have, point at what's coming**, not the other way around. Senior engs notice the gap and trust drops.
- `[note]` Two "how to run" sections (a teaser + the real walkthrough) is a common drift pattern — each gets edited independently and they slowly diverge. One canonical location is more maintainable.

**Process learnings:**
- `[insight]` Asking the assistant to **read the README from a senior-eng candidate's perspective** before shipping the LinkedIn promo flushed out 6 issues that none of the prior shipping passes (v0.9.2/0.9.3/0.9.4) caught — even though those passes also touched the README. The prior passes were author-mode (fix what I notice while editing); the review pass was reader-mode (skim like the actual audience). Different mode, different findings. Worth running explicitly before any "front-door" surface change.
- `[note]` Three patches in a row (v0.9.3 disclaimer, v0.9.4 CONTRIBUTING split, v0.9.5 review pass) all polishing the public surface before sharing — this is the right cadence for pre-promotion polish. Each one was small enough to ship cleanly; bundling them into one release would have made the diff hard to review and the devlog hard to read.

---

## v0.9.4 — CONTRIBUTING.md split + README tightening (2026-04-28 17:30)

**Review:** not yet

**What was built:**
- **New `CONTRIBUTING.md` at repo root** — covers mode awareness (don't accidentally trip `start mock interview` while developing), dev-mode kickstart prompts (orientation prompt + "I know what I want" prompt), repo orientation (framework layer vs project layer + the strict "project depends on framework, never reverse" rule), common tasks (adding a project, editing protocol/rubric/roadmap), conventions (versioning, devlog, NOTE-file gitignore, tool-agnostic candidate side), and PR guidance.
- **README "Kickstart prompts" → "To work on the tool itself"** — collapsed the two dev-mode prompts (orientation + know-what-you-want) into a one-line pointer to `CONTRIBUTING.md`. Trims roughly 18 lines from the README.
- **README "Contributing" section** — replaced the prose pointing at `roadmap.md` and `projects/README.md` with a one-line pointer to `CONTRIBUTING.md` (which then forwards to those).
- **README "About" → "About Author"** — retitled and dropped the `**Author:**` bold prefix (since the section only contains author info, the prefix was redundant).
- **README clone command** — replaced `<repo-url> sans_ai_mock` placeholder with the real `https://github.com/SansWord/sans_ai_mock.git`. Dropped the explicit target dir since the default derived from the URL is already `sans_ai_mock`.
- **`roadmap.md`** — `CONTRIBUTING.md` backlog item crossed off with `(v0.9.4 — ...)` strikethrough following the v0.9.2 convention.

**Key technical learnings:**
- `[insight]` GitHub auto-detects `CONTRIBUTING.md` at the repo root and surfaces it on the Issues / PR / "New issue" pages. That's the dominant OSS convention and the reason to prefer it over `DEV.md` or `docs/CONTRIBUTING.md` — same content, free distribution boost.
- `[note]` Splitting README into "use the tool" vs "extend the tool" matches the natural user mental model. Practitioners arriving from a LinkedIn post don't care about adding projects; contributors arriving from `roadmap.md` don't need the candidate-side workflow tips. Two docs, two audiences, less skim friction for both.

**Process learnings:**
- `[note]` Three quick patches in a row (v0.9.2 trigger-phrase + Bash allowlist, v0.9.3 disclaimer + audit recipe, v0.9.4 CONTRIBUTING split) all polish the public-facing surface in preparation for sharing on LinkedIn. A repo's "first impression" surface (README + tag/release page) is worth a focused polish pass before promotion — every confusing line costs you a portion of the visitors who bounce.

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
