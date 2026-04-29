_VALID_STATUSES = ("active", "completed")


class Todo:
    def __init__(self, title, completed=None, status=None):
        if completed is not None and status is not None:
            raise ValueError("pass either completed or status, not both")
        if status is not None and status not in _VALID_STATUSES:
            raise ValueError(f"unknown status: {status!r}")

        self.title = title
        if status is not None:
            self.status = status
        elif completed is not None:
            self.status = "completed" if completed else "active"
        else:
            self.status = "active"

    @property
    def completed(self):
        return self.status == "completed"

    @completed.setter
    def completed(self, value):
        self.status = "completed" if value else "active"

    def __repr__(self):
        return f"Todo({self.title!r}, status={self.status!r})"


class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, title):
        self._todos.append(Todo(title))

    def complete(self, index):
        self._todos[index].completed = True

    def remove(self, index):
        return self._todos.pop(index)

    def list(self, status=None):
        if status is not None and status not in _VALID_STATUSES:
            raise ValueError(f"unknown status: {status!r}")
        if status is None:
            return list(self._todos)
        return [t for t in self._todos if t.status == status]
