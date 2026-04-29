# 002 — Plan: Remove a todo by index

Files touched: `todo.py`, `test_todo.py`. No new files.

## Note on implementation shape

`list.pop(index)` already does everything the spec requires:
- Returns the removed item.
- Raises `IndexError` on out-of-range (positive and negative) and on empty list.
- Supports negative indices (`-1` = last item).
- Shifts remaining items in place.

So `TodoList.remove` will be a one-liner delegating to `self._todos.pop(index)`. The plan is therefore test-heavy and impl-light.

## Steps

1. **Tests (red): write all six tests before any impl.** All will fail with `AttributeError: 'TodoList' object has no attribute 'remove'`. Write in this order, run after each to confirm red:

   - `test_remove_returns_todo` — `add("a")`, `remove(0)` returns a `Todo` with `title == "a"`.
   - `test_remove_front` — 3-item list, `remove(0)` leaves the last two in order.
   - `test_remove_middle` — 3-item list, `remove(1)` leaves first and last; then `complete(0)` operates on what was the first (index shift confirmed).
   - `test_remove_last` — 3-item list, `remove(2)` leaves the first two; `remove(-1)` on a fresh 3-item list also removes the last (same assertion, two parametrize cases).
   - `test_remove_negative_index` — `remove(-1)` returns the last todo by title.
   - `test_remove_invalid_index_raises` — parametrized with `pytest.raises(IndexError)` for: empty list (`remove(0)`), positive out-of-range (`remove(3)` on a 3-item list), negative out-of-range (`remove(-4)` on a 3-item list).

   **Stop for review of all tests before proceeding.**

2. **Impl (green): add `remove` to `TodoList`.** Single method:

   ```python
   def remove(self, index):
       return self._todos.pop(index)
   ```

   Run full suite — all red tests go green in one shot. Existing 20 tests still pass. **Stop for review.**

3. **Verify.** Re-read `002-remove-todo.spec.md`. Confirm: all spec behaviors covered by tests, no changes to `add` / `complete` / `list` signatures, no extra surface area, full suite green.
