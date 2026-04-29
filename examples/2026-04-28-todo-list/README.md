# Example run — todo-list — 2026-04-28

A real 60-min mock of the `todo-list` project, lightly redacted for publication. The round shipped F1 + F2, dropped F3 due to scope-creep on F1.

## Outcome

**Borderline.** Process discipline (spec/plan/TDD, edge-case rigor, push-back on the AI) was strong; outcome (didn't ship F3) fell below the project's pass anchor. See [`feedback.md`](feedback.md) for the full read.

## Read order

If you're a candidate evaluating whether to try this kit, this is the order that makes the artifacts most legible:

1. **[`feedback.md`](feedback.md)** — the end-of-mock feedback the interviewer wrote. The headliner. If you only read one file, read this one.
2. **[`001-status-field.spec.md`](001-status-field.spec.md)** + **[`001-status-field.plan.md`](001-status-field.plan.md)** — F1 spec and plan, written by the candidate. The plan is the one the feedback praises ("8 numbered TDD steps with explicit Decision point markers") and the spec is the one whose scope crept ("status enums" was explicitly out of scope; the candidate built the field anyway). Reading them with the feedback open shows what the rubric is actually scoring.
3. **[`002-remove-todo.spec.md`](002-remove-todo.spec.md)** + **[`002-remove-todo.plan.md`](002-remove-todo.plan.md)** — F2 spec and plan. Tighter scope, one-line implementation justified upfront. Contrasts directly with F1.
4. **[`todo.py`](todo.py)** + **[`test_todo.py`](test_todo.py)** — final state at the end of the round (after F1 + F2; F3 not implemented). 50 lines of impl, ~210 lines of tests.

## What this demonstrates

- **What "honest feedback" looks like.** The feedback file calls out a real failure mode (scope-creep) without softening, and the verdict is "borderline" rather than "great job!" Senior-eng readers asking "is the rubric real or vague?" get a concrete answer here.
- **How the spec → plan → test → impl loop unfolds in practice.** F1's plan went over-scope (8 steps for a 5-line feature); F2's plan correctly recognized `list.pop()` did the work and stayed tiny. Same workflow shape, two different outcomes — readable as a pair.
- **What 58 minutes of pair-programming with Claude Code produces.** Concrete reference for "how much should I expect to ship in a round."

## Cost (API usage)

This run consumed roughly **$19 in API credits during the 60-min coding window** (interviewer + candidate sessions combined). Including Phase 1 setup and Phase 3 feedback delivery, the full experience came to about **$26**.

| Slice | Side | Model(s) | Input | Output | Cache write (1h) | Cache read | Cost |
|---|---|---|---:|---:|---:|---:|---:|
| 60-min coding window | Interviewer | Opus 4.7 | 67 | 6,403 | 18,686 | 1,167,742 | **~$2.79** |
| 60-min coding window | Candidate | Opus 4.7 (92 msgs) | 237 | 34,171 | 140,054 | 5,709,543 | ~$15.33 |
| 60-min coding window | Candidate | Sonnet 4.6 (26 msgs) | 46 | 6,886 | 64,616 | 1,798,909 | ~$1.03 |
| **60-min coding window** | **Combined** | | | | | | **~$19.15** |
| Full interviewer mode (~1h 27m) | Interviewer | Opus 4.7 | 182 | 27,542 | 83,024 | 3,478,592 | ~$9.78 |
| **Full experience** | **Combined** | | | | | | **~$26.14** |

Notes:

- **Pricing assumed:** Opus 4 family — input $15 / output $75 / cache_write_1h $30 / cache_read $1.50 per MTok. Sonnet 4 family — input $3 / output $15 / cache_write_1h $6 / cache_read $0.30 per MTok. Verify current rates on Anthropic's pricing page before using these as a budget.
- **Cache reads dominate (~50% of cost).** Mostly the system prompts + protocol files being re-read each turn. This is the cheap-token side of the ledger; without prompt caching, the same usage would cost roughly 10x more on the read path.
- **This is one real candidate's run.** It included F1 over-engineering (43 min on a 10-min-budgeted feature, per the feedback file). A tighter run would cost less; a longer or more iterative run would cost more.
- **Claude Code subscription vs raw API:** the dollar figures above are API-equivalent. On a Claude Code Pro or Max plan, usage is charged against your plan's quota rather than billed directly. Rough fit:
  - **Pro ($20/mo)** — tight; a single 60-min mock will likely exhaust your 5-hour rolling window before the round finishes. Undersized for serious mock practice.
  - **Max 5x ($100/mo)** — comfortable. ~1 mock per 5-hour window with headroom.
  - **Max 20x ($200/mo)** — plenty of room; multiple mocks per 5-hour window.
  - Anthropic does not publish exact quotas and adjusts them periodically — these are best-effort estimates from this run, not commitments.
- **Numbers measured by parsing the session JSONLs at `~/.claude/projects/<encoded-path>/`** (deduped by `message.id` to avoid counting the same assistant turn twice).

## Caveats

- One run, one candidate. Not a benchmark — a single data point.
- Lightly redacted: the feedback's "your project CLAUDE.md" reference was clarified to disambiguate from the framework's `CLAUDE.md`. Otherwise unchanged.
- The candidate's own CLAUDE.md (the pair-programmer system prompt that shaped Claude's behavior) is not included here. That's a stylistic artifact worth showing separately if/when we ship a "bring your own prompt" companion example.
