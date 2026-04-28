# Feature Roadmap (interviewer-only)

> **Do not show this file to the candidate.** Drop one feature at a time. When you drop, copy ONLY the `### Spec` block — never the surrounding context (base/stretch labels, expected time, what to look for).

The starter project ships with `todo_feature.md` already containing Feature 1's spec, so the candidate has something to start on without you doing anything. For each subsequent feature (F2, F3, etc.), **paste the feature's `### Spec` block in chat** — don't try to edit the candidate's `todo_feature.md` (you don't have write permission there, and editing it mid-mock is fragile). The candidate can save the pasted spec into a fresh file in their workspace if they want.

## Targets

- **3 base features** → must complete for "Pass". Aim to finish these in ~40-45 min.
- **2 stretch features** → optional. Drop only if time allows. The candidate should NOT be told these are stretch.

---

## Feature 1 — Filter todos by status (BASE, ~10 min)

### Spec

```markdown
# Feature: Filter todos by status

## Background
The team uses TodoList in a few internal tools. Right now `list()` returns every todo, but the most common workflow is: a user wants to see only the todos they still need to do. They end up filtering on the calling side, which is repetitive across callers.

## Requirements
Update `TodoList.list()` to accept an optional `status` parameter:
- `tl.list()` — returns all todos (current behavior, unchanged)
- `tl.list(status="active")` — returns only todos that are NOT completed
- `tl.list(status="completed")` — returns only todos that ARE completed

The returned list should still be a copy.

## Out of scope
- Persistence, priority, due date, tags, status enums

## Acceptance
1. All existing tests still pass.
2. New behavior covered by tests.
3. API change is backward-compatible.
```

### What to look for

- Does the candidate write a spec / plan, or jump straight to code? (Spec discipline)
- Does the pair programmer suggest a `dict` lookup or `match/case` for status — does the candidate accept blindly or pick the simplest form?
- How do they handle unknown status values? (Raise? Default to all? Empty list?) The spec deliberately leaves this open. A good candidate names the choice and defends it.
- Did they run existing tests after the change?

---

## Feature 2 — Remove a todo by index (BASE, ~10 min)

### Spec

```markdown
# Feature: Remove a todo

## Background
Users sometimes add a todo by mistake or want to discard one without marking it completed. We want a way to remove an entry from the list.

## Requirements
Add a method `tl.remove(index)`:
- Removes the todo at the given index
- Returns the removed Todo object

## Out of scope
- Removing by title or by tag
- Bulk removal

## Acceptance
1. Existing tests still pass.
2. Removing shifts remaining indices (i.e., `remove(0)` then `complete(0)` operates on the previously-second todo).
3. Tests cover: remove from middle, remove first, remove last, behavior when index is invalid.

## Notes for the implementer
There's no strict requirement on what to do with an out-of-range index. Pick a behavior, defend it briefly when you decide.
```

### What to look for

- Edge case discipline: empty list, negative index, out-of-range positive index, len(list)-1.
- Do they explicitly think through the "indices shift" issue? It's subtle — if they don't notice, it's a yellow flag.
- Did they consider returning `None` vs raising vs returning the removed Todo? The spec asks for the removed Todo — did they do that, or did the pair programmer pick something else and they didn't catch it?

---

## Feature 3 — Persistence to JSON (BASE, ~15 min)

### Spec

```markdown
# Feature: Save and load to JSON

## Background
Currently TodoList lives in memory only. Users want to persist their todos between sessions.

## Requirements
Add two methods to TodoList:
- `tl.save_to_file(path)` — writes the current todos to the given file path as JSON
- `TodoList.load_from_file(path)` — class method, returns a new TodoList with the contents of the file

The on-disk format should be human-readable JSON. You decide the schema.

## Out of scope
- Concurrent writes / locking
- Compression / encryption
- Versioning / migration

## Acceptance
1. Existing tests still pass.
2. Round-trip: save then load yields a TodoList equal to the original (same titles, same completed states, same order).
3. Tests cover: empty list round-trip, mixed completed/active round-trip, loading a file that doesn't exist (decide and document the behavior).

## Notes for the implementer
You'll need to decide the JSON schema. Two reasonable options: list of dicts, or a wrapper object. Pick one and defend it.
```

### What to look for

- Does the candidate over-engineer? (Pickle? YAML? Custom serializer?) JSON is in the spec — anything else is scope creep.
- Schema design: did they think about what happens if the file format changes later? A flat list of `{title, completed}` is simplest. Wrapping in `{"version": 1, "todos": [...]}` is forward-thinking but YAGNI for this scope.
- Missing-file behavior: did they raise, return empty, or something else? Did they pick and defend?
- Did they actually test the round-trip, or just test that save writes a file?
- Pair-programmer push-back: Claude often suggests `dataclasses` and `asdict()` here. Did the candidate accept reflexively, or evaluate?

---

## Feature 4 — Tags (STRETCH, ~15 min)

### Spec

```markdown
# Feature: Tags on todos

## Background
Users want to categorize todos. We're adding a simple tagging system.

## Requirements
- A todo can have zero or more tags (strings).
- Update `tl.add(title, tags=...)` to accept an optional list of tags. Defaults to empty.
- Update `tl.list(tag=...)` to accept an optional tag filter. When provided, return only todos that have that tag.
- The status filter and tag filter must be combinable: `tl.list(status="active", tag="work")` returns active todos tagged "work".

## Out of scope
- Tag autocomplete
- Removing tags from existing todos
- Tag aliases / case insensitivity (decide a behavior)

## Acceptance
1. Existing tests still pass.
2. Round-trip with persistence still works (tags survive save/load).
3. New tests cover: add with no tags, add with one tag, add with multiple tags, filter by tag, combined filter.
```

### What to look for

- Did they update `save_to_file` / `load_from_file` to handle tags? If they don't realize this dependency, it's a yellow flag.
- Do their tests actually cover the combined filter, or only single filters?
- How do they handle the case sensitivity question? (Spec leaves it open.)
- Did they touch the `Todo` class without thinking about backward compatibility for existing JSON files? (Real-world consideration the spec didn't ask about — bonus if they raise it.)

---

## Feature 5 — Undo last operation (STRETCH, ~15-20 min)

### Spec

```markdown
# Feature: Undo last operation

## Background
Users sometimes do something they didn't mean to — wrong remove, wrong complete, etc. We want a single-level undo.

## Requirements
- Add `tl.undo()` — reverses the most recent state-changing operation.
- "State-changing" means: `add`, `complete`, `remove` (and any new ones added by tags).
- Undo only one step. Calling `undo()` twice without an intervening op is a no-op (or raises — your choice).

## Out of scope
- Redo
- Multi-level undo / unbounded history
- Undoing reads (e.g., undoing `list()` makes no sense)

## Acceptance
1. Existing tests still pass.
2. Tests cover: undo after add, undo after complete, undo after remove, undo twice in a row, undo on empty list.

## Notes for the implementer
Many ways to implement this — snapshot the whole list before each op (simple but memory-heavy), or record an inverse op (lighter but more code). Pick one and defend.
```

### What to look for

- This feature touches every state-changing method. Did the candidate refactor cleanly (decorator? wrapper? explicit save in each method?) or copy-paste snapshot logic in three places?
- Did the pair programmer suggest the Command pattern? Did the candidate evaluate vs the simpler snapshot approach?
- Test rigor: did they test "undo on empty"? "Undo twice"?
- Memory consideration: did they bound history at 1, or accidentally save unbounded?

---

## Time-allocation guide for the interviewer

| Phase | Target time | Cumulative |
|-------|-------------|-----------|
| Setup + briefing | 3 min | 3 |
| F1 (filter) | 10 min | 13 |
| F2 (remove) | 10 min | 23 |
| F3 (persistence) | 15 min | 38 |
| Buffer / probing questions | 5 min | 43 |
| F4 (tags) — if time | 12 min | 55 |
| Feedback | 5 min | 60 |

If F1-F3 take longer than 38 min, skip stretch goals entirely and start feedback at 50-55 min so the candidate gets useful feedback. Don't sacrifice feedback quality for one more feature.

If F1-F3 finish under 30 min, the candidate is fast — drop both stretch features (F4 then F5) and assess at full pace.
