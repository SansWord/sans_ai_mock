# Feedback — todo-list — 2026-04-28

## Round summary
- Project: todo-list
- Date: 2026-04-28
- Features completed: F1 (filter by status), F2 (remove by index)
- Features attempted but not finished: F3 (persistence) — dropped due to time
- Total time: 58 min (13:37 → 14:35)
- Pair-programmer tool: Claude Code (Opus on F1, switched to Sonnet 4.6 mid-round for F2)

## What went well

- **Spec and plan discipline is genuinely strong.** Wrote both `NNN-<slug>.spec.md` and `NNN-<slug>.plan.md` for both features. F1's plan had 8 numbered TDD steps with explicit "Decision point" markers. F2's plan correctly recognized `list.pop()` did everything the spec needed and went one-line in implementation — that's good language fluency, not laziness.
- **Push-back is real and substantive.** Multiple instances per feature: challenged `_UNSET` sentinel ("can we just check if it is None?"), caught a property/setter naming collision ("we have two methods with the same name: 'completed' is that an issue?"), asked the meta-prompt "verify plan with spec first, does it fulfill spec?", probed edge cases pre-coding ("what happened if I call `remove(-3)` in a 3-item list?"), tightened a thin assertion ("can you check what's left in todo list after remove an item?").
- **Edge-case rigor is strong, especially on F2.** Empty list, positive out-of-range, negative out-of-range, negative-from-end happy path — all named and tested.
- **Routed ambiguity to the interviewer, not the AI.** When `IndexError` vs custom exception came up, and when negative-index semantics came up, asked the interviewer. Design decisions belong to the human, not the pair programmer.
- **TDD was real, not theatre.** Tests were written before impl, batched for review ("proceed and generate all red tests so I can review together").

## What to improve

- **F1 scope creep was self-inflicted, and it cost F3.** The given spec said "Update `TodoList.list()` to accept an optional `status` parameter" and explicitly listed **"status enums"** as out of scope. First prompt to Claude was *"my understanding is to add status into Todo, and the default should be 'active'"* — already past the actual ask. Built a full `status` field, constructor kwarg, validation, property/setter, and 14 new tests. Minimum-viable diff was ~5 lines. The defense ("more general in the future") is YAGNI; the spec called this out as out of scope.
  - Cost: 43 min on F1 vs. 10 budgeted. F3 didn't happen because of this single decision.
- **Watch for the candidate-led over-engineering pattern.** Less common than "AI led the candidate over a cliff," and harder to coach against because the discipline looks impeccable. Re-read the given spec out loud, then ask: "what's the minimum diff that satisfies acceptance #1, #2, #3?"
- **Introduced pytest as a dependency without flagging it.** Added `import pytest`, `pytest.raises`, `parametrize`; deleted the plain-runner block. Defensible but unilateral — in a real codebase, this is a code-review conversation. Surface tradeoffs like this to the human before committing.

## Red / yellow flags

- 🟥 Scope-creep that ignores an explicit "out of scope" line. In a real PR this would be a request-changes review.
- 🟥 Did not complete F3 (one of three required base features per the project's pass anchor).
- 🟨 Switched models mid-round to manage verbosity — pragmatic, but suggests F1's plan length wasn't fully under prompt-side control.
- 🟨 Introduced a test-framework dependency without flagging it as a tradeoff.

## Verdict

**Borderline — depends on bar.**

Process discipline is excellent, possibly Strong Pass-grade in isolation. Outcome (didn't ship F3) is Below Bar by the project's pass/fail anchor. A real interviewer's read depends on whether they weight "great process, missed scope" or "shipped on spec." The good news: this is the easier failure mode to fix — the discipline is already there, the missing piece is treating the spec as a contract rather than a starting point.

## Q&A

- **Q:** Can we try todo-list again later — would it harm the next practice or should we use a new question?
  **A:** Re-running todo-list still measures workflow signal cleanly (especially the "stay inside the out-of-scope line" muscle), but degrades the unprompted-push-back signal because you now know F3 is persistence and that Claude reflexively pushes `dataclasses` there. Recommendation: do a constrained re-run of todo-list (hard 10-min budget on F1, don't touch the `Todo` class) as deliberate practice, then move to a fresh project to re-measure unprompted dimensions.

- **Q:** Any suggestions on the prompts I gave to the pair programmer?
  **A:** Strengths: meta-verification prompts ("verify plan with spec first"), challenge-with-alternative prompts ("can we just check if it is None?"), explicit batching for review ("generate all red tests so I can review together"), and pre-stating constraints before asking for design ("BTW, let's raise IndexError"). Weaknesses: F1 opener committed to scope creep before Claude saw the spec; no upstream scope constraints ("don't add attributes to `Todo`"); no minimum-viable framing ("smallest diff that satisfies acceptance"); no artifact-length constraints (F1 plan was 31 lines for a 5-line implementation). Pattern: prompted for *quality*, but not for *restraint*. Adding restraint constraints upstream would have saved 30+ min.

- **Q:** What should I add to my CLAUDE.md for the pair programmer?
  **A:** In priority order: (1) Scope discipline rules — quote out-of-scope lines back, default to minimum diff, no "future flexibility" justifications; (2) Workflow shape — encode the spec → plan → test → impl loop with stop-after-each-step requirement; (3) Verification-before-done — trace each diff line to a spec requirement; (4) Prompt-side defaults — smallest diff wins, no new dependencies, no out-of-scope refactors; (5) Push-back symmetry — the AI should push back on you when *you* contradict the spec or workflow. Don't add all five at once; start with #1 since it directly addresses the F1 failure. Test the rules by re-running a feature and checking whether Claude actually applies them.

## Action items

- [ ] Add the "Scope discipline" rule block to your candidate-workspace CLAUDE.md (the one that loads in your pair-programmer session — not the framework's `CLAUDE.md` in the `sans_ai_mock` repo). Top of the file, before any other rules.
- [ ] For the next 3 features you build (this project or any other), write a one-sentence "minimum viable diff" *above* your spec file. If your spec adds anything not in the MVD, justify it explicitly before writing it.
- [ ] Add this constraint to your standard opening prompt: *"Quote the spec's acceptance criteria and out-of-scope sections back to me before proposing any approach. Do not propose an approach yet."*
- [ ] Practice F3 (persistence) on this project specifically — it's the highest-signal feature for "evaluate over-engineered AI suggestions" because Claude reflexively suggests `dataclasses` and `asdict()`. Goal: a 15-min implementation using a flat list-of-dicts schema, defended in one sentence.
- [ ] After 1–2 weeks, re-attempt the round on a fresh project (todo-list contamination aside) with a self-imposed budget table (F1: 10 min, F2: 10 min, F3: 15 min). Hard-stop and move on at the budget — the goal is calibration, not completion.
- [ ] Add a constraint to your AI prompts limiting plan/spec length: *"Plan ≤8 bullets, spec ≤15 lines unless I authorize more."* Re-run F1 with this constraint to see if it forces tighter scoping.
