import unittest
from task import Task, TodoList

class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task('Test Task', 'This is a test task.')
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task.')
        self.assertFalse(task.completed)

    def test_task_completion(self):
        task = Task('Test Task')
        task.mark_completed()
        self.assertTrue(task.completed)


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()
        self.task1 = Task('Task 1')
        self.task2 = Task('Task 2')

    def test_add_task(self):
        self.todo_list.add_task(self.task1)
        self.assertIn(self.task1, self.todo_list.tasks)

    def test_remove_task(self):
        self.todo_list.add_task(self.task1)
        self.todo_list.remove_task(self.task1)
        self.assertNotIn(self.task1, self.todo_list.tasks)

    def test_get_pending_tasks(self):
        self.todo_list.add_task(self.task1)
        self.todo_list.add_task(self.task2)
        self.task1.mark_completed()
        pending_tasks = self.todo_list.get_pending_tasks()
        self.assertIn(self.task2, pending_tasks)
        self.assertNotIn(self.task1, pending_tasks)

    def test_get_completed_tasks(self):
        self.todo_list.add_task(self.task1)
        self.todo_list.add_task(self.task2)
        self.task1.mark_completed()
        completed_tasks = self.todo_list.get_completed_tasks()
        self.assertIn(self.task1, completed_tasks)
        self.assertNotIn(self.task2, completed_tasks)

if __name__ == '__main__':
    unittest.main()
