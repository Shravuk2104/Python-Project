# task_manager.py
'''self is used to represent an instance of the class. With this keyword, you can
access the attributes and methods of class in python '''



class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty.")
        self.tasks.append(task)

    def remove_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        del self.tasks[task_index]

    def view_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return "\n".join(f"{i + 1}. {task}" for i, task in enumerate(self.tasks))
