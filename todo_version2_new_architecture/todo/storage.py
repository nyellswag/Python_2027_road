class TaskStorage:
    def __init__(self):
        self.tasks = []
    
    def __len__(self):
        return len(self.tasks)
    
    def __getitem__(self, index):
        return self.tasks[index]
    
    def __iter__(self):
        for task in self.tasks:
            yield task
        
    def add(self, task):
        self.tasks.append(task)
    
    def remove(self, title):
        for i, task in enumerate(self.tasks):
            if task.title.upper() == title.upper():
                del self.tasks[i]
                return
        raise ValueError("Такой задачи не существует")
    
    def find_by_title(self, title):
        for task in self.tasks:
            if task.title.upper() == title.upper():
                return task
        raise ValueError("Такой задачи не существует")
    
    def get_urgent_tasks(self):
        found = False
        for task in self.tasks:
            if task.features.priority == 'urgent':
                found = True
                yield task
        if not found:
            raise ValueError("Нет срочных задач")

    def pending_tasks(self):
        for task in self.tasks:
            if not task.completed:
                yield task
    
    def all_tasks(self):
        for task in self.tasks:
            yield task
