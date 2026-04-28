# Todo Library — AI round practice project

This is a tiny, working Python library for managing todos. It's intentionally minimal so you can practice the AI round workflow on incremental feature additions without spending time understanding the domain.

## Files

- `todo.py` — core library (one class, three methods)
- `test_todo.py` — tests for the current behavior, all passing
- `todo_feature.md` — **the next feature you'll be adding** (start here)

## How to use this for AI round practice

1. Copy these files into a fresh working directory of your choice. Initialize git there (`git init && git add . && git commit -m 'initial'`) so the interviewer can inspect diffs.
2. Run `python -m pytest test_todo.py` (or `python test_todo.py` if you wire up a `__main__`) — confirm baseline tests pass.
3. Open `todo_feature.md` and run the **full pair-programming workflow**:
   - Read the spec carefully, ask clarifying questions out loud
   - Draft a `feature.spec.md` (your own re-statement of the ask)
   - Draft a `feature.plan.md` (steps you'll take)
   - Write tests first (TDD)
   - Implement
   - Verify
4. When you finish the first feature, ask for the next one — there are more features lined up. They'll be released one at a time so you don't see the whole roadmap at once.

## Current behavior

```python
from todo import TodoList

tl = TodoList()
tl.add("buy milk")
tl.add("write report")
tl.complete(0)
print(tl.list())   # both todos, the first marked completed
```

That's it. No persistence, no priorities, no tags. Just enough to be a real codebase you can extend.
