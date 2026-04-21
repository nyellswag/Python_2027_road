import datetime
from dataclasses import dataclass, field
from enum import Enum

class TaskNotFoundError(Exception):
    pass

class TaskStatus(Enum):
    TODO='todo'
    IN_PROGRESS="in_progress"
    DONE="done"
    CANCELLED='cancelled'

@dataclass
class TaskFeatures:
    deadline:int = None
    priority: str = 'normal'
    tags: list = field(default_factory=list)

@dataclass
class Task():
    title: str
    completed: bool = False
    status: TaskStatus = TaskStatus.TODO
    features: TaskFeatures = field(default_factory=TaskFeatures)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    @property
    def display_info(self):
        status = "✔" if self.completed else " "
        date = self.created_at.strftime("%Y-%m-%d")
        return f"[{status}] {self.title} ({date})"
    
    @property
    def is_urgent(self):
        return self.features.deadline is not None
    
    def mark_completed(self):
        self.completed = True
        self.status = TaskStatus.DONE
       

class TodoManager():
    total_managers_created = 0

    def __init__(self):
        self.storage = TaskStorage()
        TodoManager.total_managers_created += 1

    def add_task(self, title, deadline=None, priority="normal", tags=None):
        TodoManager.validate_title(title)
        features = TaskFeatures(deadline, priority, tags)
        task = Task(title, features=features)

        self.storage.add(task)
    
    def show_all(self):
        return self.storage.show_tasks()
    
    def show_pending(self):        
        return self.storage.pending_tasks()
    
    
    def mark_done(self, title: str):
        task = self.storage.find_by_title(title)
        task.mark_completed()
    
    def delete_task(self, title: str):
        self.storage.remove(title)
    

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


class TaskStorage:
    def __init__(self):
        self.tasks = []

    def __len__(self):
        return len(self.tasks)
    
    def __getitem__(self, index):
        return self.tasks[index]
    
    def __iter__(self):
        return (task for task in self.tasks)

    def add(self, task):
        self.tasks.append(task)

    def remove(self, title: str):
        for i, task in enumerate(self.tasks):
            if task.title.upper() == title.upper():
                del self.tasks[i]
                return
        raise TaskNotFoundError("Такой задачи не существует")
    
    def find_by_title(self, title: str):
        for task in self.tasks:
            if task.title.upper() == title.upper():
                return task
        
        raise TaskNotFoundError("Такой задачи не существует")
    
    def get_urgent_tasks(self):
        found = False

        for i, task in enumerate(self.tasks, 1):
            if task.is_urgent:
                found = True
                yield f"{i}. {task.display_info} | days till deadline: {task.features.deadline}"

        if not found:
            raise ValueError("Нет срочных задач")
    
    def show_tasks(self):
        if not self.tasks:
            raise ValueError("Лист пустой")
        
        for i, task in enumerate(self.tasks, 1):
            yield f"{i}. {task.display_info}"

    def pending_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            if not task.completed:           
                yield f"{i}. {task.display_info}"
