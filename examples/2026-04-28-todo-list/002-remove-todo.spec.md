# 002 — Remove a todo by index

## Inputs / outputs

- `TodoList.remove(index)` removes the todo at `index` and returns the removed `Todo` object.
- `index` follows standard Python list semantics: non-negative integers count from the front, negative integers count from the back (`-1` = last item).
- If `index` is out of range (including any index on an empty list), raise `IndexError`.
- After removal, remaining todos shift down to fill the gap — subsequent calls use the new indices.

## Observable behavior

- `remove(0)` on a 3-item list returns the first todo; `list()` then returns the remaining two in original order.
- `remove(-1)` returns the last todo; remaining items are unaffected.
- `remove(1)` on a 3-item list returns the middle todo; `remove(0)` afterward operates on what was originally the second todo.
- `remove(index)` on an empty list raises `IndexError`.
- `remove(index)` where `index >= len(list)` or `index < -len(list)` raises `IndexError`.
- `add` / `complete` / `list` signatures and behavior are unchanged.

## Out of scope

- Removing by title or tag.
- Bulk removal.
- Any return value other than the removed `Todo` object.

## Success criterion

Full test suite passes. New tests cover: remove from middle, remove from front, remove from last, index-shifting after removal, and `IndexError` on invalid index (out-of-range positive, out-of-range negative, empty list). All existing tests pass without modification.
