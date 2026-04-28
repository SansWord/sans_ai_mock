# Feedback Rubric

> Used by the interviewer at the end of the mock to give structured, honest feedback. Candidate may also read this after the mock to self-evaluate.

The AI-pair-programming round assesses **how the candidate directs and verifies an AI agent**, not just whether they can write code. The agent will write most of the code; the candidate's job is to scope it, push back when wrong, verify it works, and own the result.

## Six assessment dimensions

### 1. Spec & plan discipline

Does the candidate write a spec before coding? A plan before implementing? Or do they jump straight to "Claude, write me X"?

- **Strong**: Always writes a brief spec + plan, even for "simple" features. Names tradeoffs explicitly.
- **OK**: Writes a spec for harder features, skips for easy ones.
- **Weak**: Skips spec entirely, no plan, just describes the feature to the pair programmer and accepts whatever comes back.

🟥 Red flag: starts coding immediately on every feature without scoping.

### 2. Prompt quality

Are the candidate's prompts to the pair programmer specific, contextual, and constrained? Or vague and underspecified?

- **Strong**: Includes constraints ("don't use external libraries", "match the existing test style"), references existing code, asks for tradeoffs.
- **OK**: Clear asks but missing constraints; pair programmer occasionally over-engineers.
- **Weak**: One-sentence asks, no context, accepts whatever comes back.

🟨 Yellow flag: prompts that lead to over-engineering the candidate doesn't catch.

### 3. Push-back / critical evaluation

When the pair programmer suggests something — code, an approach, a refactor — does the candidate evaluate it, or accept reflexively?

- **Strong**: Pushes back at least once per feature. Asks "why" or "is there a simpler way". Rejects suggestions that don't fit.
- **OK**: Pushes back on big things, accepts small things uncritically.
- **Weak**: Accepts every suggestion. Code in the diff includes ideas the candidate can't defend.

🟥 Red flag: codebase ends up with patterns the candidate didn't ask for and can't explain.

### 4. Test discipline (process)

When are tests written, and does the candidate verify the suite? This dimension is about the **process** — whether tests come first, whether the suite is run, whether the test code reflects the candidate's intent vs. AI-generated boilerplate. **Edge-case coverage of specific cases lives in Dim 5, not here.**

- **Strong**: TDD per feature — writes a failing test, then the smallest change to pass. Runs the full suite before saying "done". Test code reflects the candidate's own spec, not just "whatever the AI generated." Reads the test diff like any other code.
- **OK**: Tests written after the code but before "done". Suite runs. Test code is reviewed.
- **Weak**: Tests added as an afterthought, or AI-generated and not reviewed. Doesn't verify the suite passes before claiming done.

🟥 Red flag: says "done" without running tests, or commits AI-generated test code the candidate can't explain.

### 5. Edge case awareness (identification + handling)

Does the candidate proactively identify edge cases the spec leaves ambiguous, decide on a behavior, and ensure that behavior is captured (in code AND in tests)? This dimension covers both the upstream identification *and* the downstream coverage. (Process-level "did they run the suite?" is in Dim 4.)

- **Strong**: Lists edge cases out loud during the spec phase. Picks behaviors and defends them ("I'll raise on out-of-range index, because silent failure would be a bug magnet"). Each named edge has a corresponding test.
- **OK**: Catches obvious edge cases when prompted by the pair programmer or interviewer. Tests cover the named edges but the candidate didn't surface them unprompted.
- **Weak**: Only handles the cases the spec explicitly mentions; misses anything subtle. Tests are happy-path only.

> **Boundary with Dim 4:** if you're scoring an observation, ask "is this about *when/how the test process ran* or *which cases were considered*?" Process → Dim 4. Cases → Dim 5. A candidate strong at one isn't automatically strong at the other.

### 6. Verification & ownership

Did the candidate actually verify the diff matches the spec? Run the tests? Inspect the changes manually before claiming "done"?

- **Strong**: Reads the diff before saying done. Runs the test suite. Catches scope creep the pair programmer introduced.
- **OK**: Runs tests but doesn't always read the diff. Trusts the pair programmer.
- **Weak**: Says "done" based on the pair programmer claiming "implementation complete". Doesn't read the diff.

🟥 Red flag: code merged that the candidate can't explain line by line.

## Summary scoring

For each dimension, pick: **Strong / OK / Weak**.

| Dimensions | Verdict |
|-----------|---------|
| 5-6 Strong, ≤1 Weak | Strong pass — would hire |
| 3-4 Strong, ≤2 Weak | Pass with notes |
| 2-3 Strong, 1-2 Weak, no red flags | Borderline — depends on bar |
| Any red flag, or 3+ Weak | Below bar — would not pass |

## Common patterns to flag

- **"Trust the AI" pattern**: candidate accepts everything, doesn't read the code, can't explain decisions. Below bar even if features work.
- **"Bypass discipline" pattern**: candidate doesn't write specs/plans/tests because "it's simple". Below bar — every feature is "simple" until it isn't.
- **"Over-prompted" pattern**: candidate writes 4-paragraph prompts for trivial asks. OK at junior level, slows them down at senior.
- **"Silent partner" pattern**: candidate doesn't push back ever, even when the pair programmer over-engineers. Yellow flag.
- **"Skip-the-tests" pattern**: claims tests would slow them down. Red flag.
- **"Spec-as-starting-point" pattern**: candidate uses excellent process (spec, plan, TDD, push-back) on a scope larger than the given spec. Adds fields, methods, or surface area the spec didn't ask for, often invoking "future flexibility" or "more general later" as justification — directly contradicting an explicit "Out of scope" line. Distinguishing tell: artifacts and discipline look strong in isolation, but the diff exceeds minimum-viable. Often co-occurs with overrunning the time budget by 2–4×, which then cascades into dropped features. Yellow flag at junior level (process is right, scope calibration takes time); red flag at senior level (a senior IC must treat the spec as a contract, not a starting point). Typical interviewer probe: *"The spec listed X as out of scope. Did you read that line, and did your implementation respect it?"*

## Time efficiency notes

Time per feature can be a signal but isn't decisive:

- **Too fast** (<5 min for a base feature): probably skipped spec / plan / tests. Check the diff.
- **Too slow** (>20 min for a base feature): probably struggling with the AI. Could be vague prompts, could be excessive iteration. Check the prompts they sent.
- **Steady**: ~10-15 min per base feature with TDD is healthy.

## Be honest

The candidate is using this mock to *improve*. Soft feedback wastes their time. If they accepted bad code without reading it, say so explicitly. If their prompts were vague, quote one and explain what was missing. If a verdict is "below bar", say it and explain what to fix.
