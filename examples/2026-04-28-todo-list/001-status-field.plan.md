# 001 — Plan: Status field on Todo + filter on list()

Files touched: `todo.py`, `test_todo.py`. No new files.

## Steps

1. **Test (red): default status is "active".** Add `test_new_todo_defaults_to_active_status` asserting `Todo("x").status == "active"` and `.completed is False`. Run suite — new test fails (no `status` attr yet); existing six pass.

2. **Impl (green): introduce `status` on `Todo`, derive `completed` from it.** Replace `completed` plain attribute with `status` storage + a `completed` property (getter returns `status == "completed"`; setter writes `"completed"` / `"active"` so legacy `todo.completed = True` keeps working and stays consistent with `status`). Constructor signature stays `__init__(self, title, completed=False)` for now — the `status` kwarg lands in step 2b. Update `__repr__` to show `status`. Run suite — all green. **Stop for review.**

2a. **Test (red): constructor accepts `status="completed"`.** Add `test_todo_constructor_accepts_status` asserting `Todo("x", status="completed").status == "completed"` and `.completed is True`. Also assert `Todo("x", status="active").status == "active"`. Fails — constructor doesn't accept `status` kwarg yet.

2b. **Test (red): constructor rejects bad input.** Add two tests, both using `pytest.raises(ValueError)`:
    - `test_todo_constructor_rejects_both_status_and_completed` — covers `Todo("x", completed=True, status="completed")` *and* the consistent-but-still-both case `Todo("x", completed=False, status="active")` (per your rule: never both, regardless of whether they agree).
    - `test_todo_constructor_rejects_unknown_status` — covers `Todo("x", status="bogus")`. Mirrors `list()`'s validation rule for consistency across the API.

    Both fail — no guards yet.

2c. **Impl (green): constructor accepts both kwargs, never together; validates status.** Use a sentinel default (`_UNSET = object()`) for both `completed` and `status`. Logic order: (1) if both are non-sentinel → `ValueError("pass either completed or status, not both")`; (2) if `status` is non-sentinel and not in `{"active", "completed"}` → `ValueError(f"unknown status: {status!r}")`; (3) if only `status` is given, store it; (4) if only `completed` is given, derive status from it; (5) if neither, default to `status="active"`. Run suite — 2a and 2b tests pass, prior tests still pass. **Stop for review.**

3. **Test (red): complete() sets status to "completed".** Add `test_complete_sets_status_to_completed` asserting that after `tl.complete(0)`, `tl.list()[0].status == "completed"` (and `.completed is True`, already covered but worth the paired assert). Fails only if step 2 regressed; expected to pass since `complete` writes via `.completed = True` → setter syncs `status`. **Decision point:** if I'd rather have `complete` write `status` directly instead of going through the boolean setter, flag it here before moving on.

4. **Test (red): list(status="active") filters to active todos.** Add `test_list_filters_active`: add three todos, complete the middle one, assert `[t.title for t in tl.list(status="active")]` returns the two uncompleted titles in order. Fails — `list()` doesn't accept the kwarg yet.

5. **Test (red): list(status="completed") filters to completed todos.** Add `test_list_filters_completed`: same setup, assert only the completed one is returned.

6. **Impl (green): add `status` kwarg to `TodoList.list()`.** Signature becomes `list(self, status=None)`. If `status is None`, return current behavior. If `status in {"active", "completed"}`, filter then return a copy. Otherwise raise `ValueError(f"unknown status: {status!r}")`. Run suite — steps 4 & 5 pass; existing copy-guarantee test still passes because we always build a new list. **Stop for review.**

7. **Test (red): unknown status raises ValueError.** Add `test_list_rejects_unknown_status` using `pytest.raises(ValueError)` (or a try/except for the no-pytest runner — match the existing test style, which is plain `assert`; use `pytest.raises` since the file already imports nothing pytest-specific but pytest is the documented runner). **Decision point:** confirm `pytest.raises` is acceptable; if you'd rather keep zero pytest imports to preserve the `__main__` runner path, I'll switch to a try/except + `assert`.

8. **Verify.** Re-read `001-status-field.spec.md`. Run full suite (`python -m pytest test_todo.py` and `python test_todo.py`). Confirm: original six tests untouched; new tests added (status default, complete-sets-status, list-active, list-completed, list-rejects-unknown, constructor-accepts-status, constructor-rejects-both, optionally constructor-rejects-unknown-status); `Todo.completed` boolean contract preserved; `list()` API backward-compatible; constructor backward-compatible for the existing `Todo(title)` and `Todo(title, completed=True)` call shapes. Diff covers spec exactly — no extra surface area.
