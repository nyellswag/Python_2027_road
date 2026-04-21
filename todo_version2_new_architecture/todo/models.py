from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field

class TaskStatus(Enum):
    TODO = 'todo'
    IN_PROGRESS = "in_progress"
    DONE = 'done'
    CANCELLED = 'cancelled'

@dataclass
class TaskFeatures:
    deadline: int = 0
    priority: str = 'normal'
    tags: list = field(default_factory=list)

@dataclass
class Task:
    title: str
    completed: bool = False
    features: TaskFeatures = field(default_factory=TaskFeatures)
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def is_completed(self):
        if self.completed == True:
            return True
        return False
    
    @property
    def is_urgent(self):
        if self.features.priority == 'urgent':
            return True
        return False
    
    @property
    def display_info(self):
        status = "✔" if self.completed else ' '
        date = self.created_at.strftime("%Y-%m-%d")
        return f"[{status}] {self.title} ({date})"
    

    def mark_completed(self):
        self.completed = True