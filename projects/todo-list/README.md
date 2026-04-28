# todo-list — interviewer notes

> **Interviewer-only.** This file is not in `start_folder/` — the candidate never sees it. For candidate-facing context, see `start_folder/README.md`.

## Metadata

| Field | Value |
|-------|-------|
| Domain | In-memory data-structure library (todo CRUD + filters + persistence) |
| Language | Python |
| Target seniority | Mid-level (IC3–IC4) — junior candidates may not finish all 3 base features in time |
| Target role | Generalist software engineer / backend-leaning |
| Round length | ~60 min including setup + feedback |
| Domain knowledge required | None — intentionally minimal so the round assesses AI-pairing skill, not domain ramp-up |

## What this project tests

This project is a baseline-difficulty round. The codebase is tiny and the domain is trivial on purpose — that strips away "do they understand the business logic?" and isolates the signal you actually want: **how the candidate works with an AI pair-programmer under time pressure.**

Concretely, across the 3 base features the candidate is expected to demonstrate:

1. **Spec / plan discipline.** Do they restate the ask, draft a plan, and write tests first — or jump straight to code with the AI? F1 (filter) is the cheapest place to observe this; if they skip the workflow on F1, it's a behavioral signal that holds for F2 / F3.
2. **AI push-back.** Will they accept the pair programmer's first suggestion (often over-engineered: `match/case`, `dataclasses`, Command pattern) or evaluate alternatives? F3 (persistence) and F5 (undo) are the highest-signal moments — the AI tends to propose elegance over simplicity.
3. **Edge-case rigor.** F2 (remove by index) is the canonical place — empty list, negative index, out-of-range. A candidate who only tests the happy path is showing you a real workflow gap.
4. **Backward compatibility instinct.** F1 changes a public method signature; F4 (stretch) re-changes the same method. Did they extend, or did they break callers? The pair programmer rarely flags this — the candidate has to.
5. **Schema / persistence judgment.** F3 forces a JSON schema decision. Watch whether they pick a simple flat shape and defend it, or accept whatever the AI outputs without thinking about future migration.
6. **Refactor vs duplicate.** F5 (stretch) touches every state-changing method — the candidate either refactors cleanly (decorator, wrapper) or copy-pastes snapshot logic three times. Both are acceptable; the signal is whether they *chose*.

## When to pick this project

- First-time candidate doing the mock — lowest cognitive overhead, fastest to ramp into.
- You want to assess **pair-programming workflow** specifically (not domain modeling, not system design).
- 60-minute round.

## When NOT to pick this project

- Candidate has signaled they want to be stretched on a harder domain — pick something with more domain depth (e.g., `bank-ledger` once added).
- You want to assess concurrency / distributed-systems / async — this project has none of that.

## Where to look

- `roadmap.md` — the 3 base + 2 stretch features, each with a `### Spec` block to drop and a "what to look for" cheat sheet. Drop one feature at a time. Stretch goals only if F1–F3 finish under ~38 min.
- `start_folder/` — the candidate-facing bundle. Inspect what they have so you know what they're working from.

## Pass / fail anchor

Time references below are cumulative, measured against the time-allocation table in `roadmap.md` (F3 ends at ~38 min, buffer extends to ~43 min, total round 60 min including feedback).

- **Pass:** all 3 base features done within the F3 budget plus buffer (~43 min cumulative), with visible spec/plan/test discipline on at least 2 of them, and at least one moment of meaningful push-back on the AI.
- **Borderline:** all 3 base features done in time but at least one was AI-driven throughout (candidate accepted the AI's first suggestion without restating, planning, or push-back). Note: the rubric in `feedback_rubric.md` would call sustained "Trust the AI" pattern Below bar — this Borderline level only applies when *one* feature drifted, not all three.
- **Fail:** could not complete F2 or F3, OR completed them but with no tests / broken existing tests / silent acceptance of AI errors.

See `feedback_rubric.md` (root) for the full 6-dimension scoring.
