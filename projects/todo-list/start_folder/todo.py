class Todo:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"Todo({self.title!r}, completed={self.completed})"


class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, title):
        self._todos.append(Todo(title))

    def complete(self, index):
        self._todos[index].completed = True

    def list(self):
        return list(self._todos)
