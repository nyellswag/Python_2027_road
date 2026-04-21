from .storage import TaskStorage
from .models import TaskFeatures, Task


class TodoManager:
    total_managers = 0

    def __init__(self):
        self.storage = TaskStorage()
        TodoManager.total_managers += 1

    def add_task(self, title: str, deadline=None, priority='normal', tags=None):
        TodoManager.validate_title(title)
        features = TaskFeatures(deadline, priority, tags)
        task = Task(title, features=features)

        self.storage.add(task)
    
    def delete_task(self, title: str):
        self.storage.remove(title)

    def mark_done(self, title):
        task = self.storage.find_by_title(title)
        task.mark_completed()

    def show_all(self):
        return self.storage.all_tasks()
    
    def show_pending(self):
        return self.storage.pending_tasks()

    def show_urgent_tasks(self):
        return self.storage.get_urgent_tasks()
    
    @classmethod
    def total_managers_created(self):
        return self.total_managers
    
    @classmethod
    def from_list(cls, tasks_list):
        manager = cls()
        for title in tasks_list:
            manager.add_task(title)
        return manager
    
    @staticmethod
    def validate_title(title):
        if len(title.strip()) == 0: 
            raise ValueError("Ваша задача пустая") 
        elif len(title) < 3: 
            raise ValueError("Ваша задача слишком короткая")
