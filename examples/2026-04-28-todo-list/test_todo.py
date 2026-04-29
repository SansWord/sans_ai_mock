import pytest

from todo import Todo, TodoList


def test_new_list_is_empty():
    tl = TodoList()
    assert tl.list() == []


def test_new_todo_defaults_to_active_status():
    t = Todo("x")
    assert t.status == "active"
    assert t.completed is False


@pytest.mark.parametrize(
    "status,expected_completed",
    [
        ("active", False),
        ("completed", True),
    ],
)
def test_todo_constructor_accepts_status(status, expected_completed):
    t = Todo("x", status=status)
    assert t.status == status
    assert t.completed is expected_completed


@pytest.mark.parametrize(
    "completed,expected_status",
    [
        (False, "active"),
        (True, "completed"),
    ],
)
def test_todo_constructor_accepts_completed(completed, expected_status):
    t = Todo("x", completed=completed)
    assert t.completed is completed
    assert t.status == expected_status


@pytest.mark.parametrize(
    "completed,status",
    [
        (True, "completed"),
        (True, "active"),
        (False, "completed"),
        (False, "active"),
    ],
)
def test_todo_constructor_rejects_both_status_and_completed(completed, status):
    # Never both, regardless of whether the values agree.
    with pytest.raises(ValueError):
        Todo("x", completed=completed, status=status)


def test_todo_constructor_rejects_unknown_status():
    with pytest.raises(ValueError):
        Todo("x", status="bogus")


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


def test_complete_sets_status_to_completed():
    tl = TodoList()
    tl.add("buy milk")
    tl.complete(0)
    todo = tl.list()[0]
    assert todo.status == "completed"
    assert todo.completed is True


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


def test_remove_returns_todo():
    tl = TodoList()
    tl.add("a")
    removed = tl.remove(0)
    assert isinstance(removed, Todo)
    assert removed.title == "a"


def test_remove_front():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    tl.remove(0)
    assert [t.title for t in tl.list()] == ["b", "c"]


def test_remove_middle():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    tl.remove(1)
    assert [t.title for t in tl.list()] == ["a", "c"]
    # index shift: complete(0) now operates on "a"
    tl.complete(0)
    assert tl.list()[0].title == "a"
    assert tl.list()[0].completed is True


@pytest.mark.parametrize(
    "index",
    [2, -1],
)
def test_remove_last(index):
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    tl.remove(index)
    assert [t.title for t in tl.list()] == ["a", "b"]


def test_remove_negative_index():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    removed = tl.remove(-1)
    assert removed.title == "c"
    assert [t.title for t in tl.list()] == ["a", "b"]


@pytest.mark.parametrize(
    "setup,index",
    [
        ([], 0),   # empty list
        (["a", "b", "c"], 3),   # positive out-of-range
        (["a", "b", "c"], -4),  # negative out-of-range
    ],
)
def test_remove_invalid_index_raises(setup, index):
    tl = TodoList()
    for title in setup:
        tl.add(title)
    with pytest.raises(IndexError):
        tl.remove(index)


def test_list_filters_active():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    tl.complete(1)
    titles = [t.title for t in tl.list(status="active")]
    assert titles == ["a", "c"]


def test_list_filters_completed():
    tl = TodoList()
    tl.add("a")
    tl.add("b")
    tl.add("c")
    tl.complete(1)
    todos = tl.list(status="completed")
    assert [t.title for t in todos] == ["b"]
    assert todos[0].status == "completed"


def test_list_rejects_unknown_status():
    tl = TodoList()
    tl.add("a")
    with pytest.raises(ValueError):
        tl.list(status="bogus")
