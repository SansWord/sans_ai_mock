# Feature: Filter todos by status

## Background

The `TodoList` library is used in a few internal tools. Right now `list()` returns every todo, but the most common workflow we see is: a user wants to see *only the todos they still need to do*, not the ones they've already completed. They end up filtering on the calling side, which is repetitive and inconsistent across callers.

We want to push that filter into the library itself.

## Requirements

Update `TodoList.list()` to accept an optional `status` parameter:

- `tl.list()` — returns all todos (current behavior, unchanged)
- `tl.list(status="active")` — returns only todos that are not completed
- `tl.list(status="completed")` — returns only todos that are completed

The returned list should still be a copy (mutating it must not affect internal state, same as today).

## Out of scope (do not implement — these have been considered and deliberately excluded)

If you find yourself adding any of the following, **stop**. Either remove the work or ask the interviewer to confirm the deviation before continuing.

- Persistence (no save/load to disk)
- Priority / due date / tags
- **Status enums or richer status types** — strings are fine on the `list()` argument. Do **not** add a `status` field, attribute, or property to `Todo`. Do **not** add a `status=` constructor kwarg. The `completed` boolean stays as the only state on `Todo`.
- Filtering by anything other than status
- Validation of unknown status strings beyond what the spec requires (pick a behavior, document it, move on)

## Acceptance

1. All existing tests still pass without modification.
2. New behavior is covered by tests.
3. The API change is backward-compatible — calling code that does `tl.list()` with no args continues to work.
4. **The diff to `todo.py` is minimal.** No new attributes on `Todo`, no new constructor kwargs, no new exception types unless required to satisfy 1–3. If your diff adds any of those, you have either misread the spec or are working past it; stop and reconsider.

## Notes for the implementer

There's no strict requirement on what to do with an unknown status string. Pick a behavior, defend it briefly when you decide.
