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

## Out of scope

- Persistence
- Priority / due date / tags
- Status enums or richer status types — strings are fine for now
- Filtering by anything other than status

## Acceptance

1. All existing tests still pass without modification.
2. New behavior is covered by tests.
3. The API change is backward-compatible — calling code that does `tl.list()` with no args continues to work.

## Notes for the implementer

There's no strict requirement on what to do with an unknown status string. Pick a behavior, defend it briefly when you decide.
