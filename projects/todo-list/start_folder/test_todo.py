from todo import Todo, TodoList


def test_new_list_is_empty():
    tl = TodoList()
    assert tl.list() == []


def test_add_creates_active_todo():
    tl = TodoList()
    tl.add("buy milk")
    todos = tl.list()
    assert len(todos) == 1
    assert todos[0].title == "buy milk"
    assert todos[0].completed is False


def test_add_preserves_insertion_order():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    titles = [t.title for t in tl.list()]
    assert titles == ["a", "b", "c"]


def test_complete_marks_todo_done():
    tl = TodoList()
    tl.add("buy milk")
    tl.complete(0)
    assert tl.list()[0].completed is True


def test_complete_does_not_affect_other_todos():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.complete(0)
    todos = tl.list()
    assert todos[0].completed is True
    assert todos[1].completed is False


def test_list_returns_a_copy():
    # External mutation of the returned list must not affect internal state.
    tl = TodoList()
    tl.add("a")
    snapshot = tl.list()
    snapshot.clear()
    assert len(tl.list()) == 1


if __name__ == "__main__":
    # Tiny runner so this works without pytest.
    import sys
    failures = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok  {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL {name}: {e}")
    sys.exit(1 if failures else 0)
