# 001 — Status field on Todo + filter on list()

## Inputs / outputs

- `Todo` gains a `status` attribute, a string that is either `"active"` or `"completed"`. New todos default to `"active"`.
- `Todo.completed` remains as a boolean and stays consistent with `status`: `completed is True` iff `status == "completed"`. Existing reads of `todo.completed` keep working.
- `TodoList.complete(index)` sets the todo's `status` to `"completed"` (and therefore `completed` to `True`).
- `TodoList.list(status=None)` accepts an optional keyword:
  - `None` (default) → return all todos, current behavior.
  - `"active"` → return only todos with `status == "active"`.
  - `"completed"` → return only todos with `status == "completed"`.
  - Any other value → raise `ValueError`.
- The returned list is still a shallow copy; mutating it must not affect internal state.

## Observable behavior

- All six existing tests in `test_todo.py` continue to pass without modification (the `completed` boolean contract is preserved).
- A fresh todo reports `status == "active"` and `completed is False`.
- After `complete(i)`, todo `i` reports `status == "completed"` and `completed is True`.
- `list("bogus")` (or any string not in `{"active", "completed"}`) raises `ValueError` before returning anything.

## Success criterion

The full test suite passes, including new tests covering the status field, the filter behavior for both valid values, and the `ValueError` on unknown input. No changes to `add` / `complete` call signatures. No new files beyond tests and the spec/plan pair.
