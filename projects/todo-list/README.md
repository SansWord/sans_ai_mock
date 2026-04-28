# todo-list — interviewer notes

> **Interviewer-only.** This file is not in `start_folder/` — the candidate never sees it. For candidate-facing context, see `start_folder/README.md`.
>
> **Scope of this file:** describes the question (domain, what's there, what it exercises, where to read). It does **not** prescribe interview format — round length, target seniority, when-to-pick, and pass/fail bar are interviewer-protocol concerns owned by `INTERVIEWER.md` and `feedback_rubric.md`. The project's per-feature time estimates live in `roadmap.md`.

## Metadata

| Field | Value |
|-------|-------|
| Domain | In-memory data-structure library (todo CRUD + filters + persistence) |
| Language | Python |
| Domain knowledge required | None — intentionally minimal so the round assesses AI-pairing skill, not domain ramp-up |

## What this project exercises

The codebase is tiny and the domain is trivial on purpose — that strips away "do they understand the business logic?" and isolates the signal that the AI-pairing rubric measures. Across the base + stretch features, this question gives the candidate room to demonstrate:

1. **Spec / plan discipline.** F1 (filter) is the cheapest place to observe this; if they skip the workflow on F1, it's a behavioral signal that holds for F2 / F3.
2. **AI push-back.** F3 (persistence) and F5 (undo) are the highest-signal moments — the AI tends to propose elegance over simplicity (`dataclasses`, Command pattern, `match/case`).
3. **Edge-case rigor.** F2 (remove by index) is the canonical place — empty list, negative index, out-of-range.
4. **Backward compatibility instinct.** F1 changes a public method signature; F4 (stretch) re-changes the same method. Did they extend, or did they break callers? The pair programmer rarely flags this — the candidate has to.
5. **Schema / persistence judgment.** F3 forces a JSON schema decision. Watch whether they pick a simple flat shape and defend it, or accept whatever the AI outputs without thinking about future migration.
6. **Refactor vs duplicate.** F5 (stretch) touches every state-changing method — the candidate either refactors cleanly (decorator, wrapper) or copy-pastes snapshot logic three times. Both are acceptable; the signal is whether they *chose*.

These map cleanly onto the dimensions in `feedback_rubric.md`. If you're picking a question to exercise specific dimensions, this one is strongest on Dim 1 (spec discipline), Dim 3 (push-back), Dim 5 (edge cases), and Dim 6 (verification).

## Where to look

- `roadmap.md` — the 3 base + 2 stretch features, each with a `### Spec` block to drop and a "what to look for" cheat sheet. Drop one feature at a time.
- `start_folder/` — the candidate-facing bundle. Inspect what they have so you know what they're working from.
- `start_folder/todo_feature.md` — F1's spec, pre-bundled in the candidate workspace. The roadmap's F1 spec block is the verbatim duplicate; keep them in sync.
