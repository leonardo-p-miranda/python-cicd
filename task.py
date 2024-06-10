class Task:
    def __init__(self, title, description=''):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task('{self.title}', '{self.description}', {self.completed})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]
