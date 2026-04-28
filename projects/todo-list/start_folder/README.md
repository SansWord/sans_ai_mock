# Todo Library — AI round practice project

This is a tiny, working Python library for managing todos. It's intentionally minimal so you can practice the AI round workflow on incremental feature additions without spending time understanding the domain.

## Files

- `todo.py` — core library (one class, three methods)
- `test_todo.py` — tests for the current behavior, all passing
- `todo_feature.md` — **the next feature you'll be adding** (start here)

## Where to start

The interviewer handed you the workspace setup commands separately — workspace creation, `git init`, and which AI tool to use are not your problem. Once your workspace is ready:

1. Confirm the baseline test suite passes: `python3 -m pytest test_todo.py` (or `python3 test_todo.py` if you wire up a `__main__`).
2. Open `todo_feature.md` — that's your first feature spec. Work through it with whatever pair-programming workflow you'd use on a real ticket (read the spec, ask clarifying questions, draft a spec/plan, write tests first, implement, verify).
3. When you finish the first feature, say **"done"** to the interviewer — they'll inspect, ask probing questions, then drop the next feature.

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
