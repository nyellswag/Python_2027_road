import datetime

class Task():
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
        self.created_at = datetime.datetime.now()

    def __str__(self):
        status = "✔" if self.completed else " "
        date = self.created_at.strftime("%Y-%m-%d")
        return f"[{status}] {self.title} ({date})"

class TaskNotFoundError(Exception):
    pass


def create_todo_manager():
    tasks = []

    def add_task(title: str):
        if title.strip() == '':
            raise ValueError("Пустая строка")
        new_task = Task(title)
        tasks.append(new_task)
    
    def show_all():
        if not tasks:
            raise ValueError("Лист пустой")
        
        for i, task in enumerate(tasks, 1):
            yield f"{i}. {task}"
    
    def show_pending():
        if not tasks:
            raise ValueError("Лист пустой")
        
        found = False
        for i, task in enumerate(tasks, 1):
                if task.completed == False:
                    found = True
                    yield f"{i}. {task}"
        if not found:
            raise ValueError("Нет невыполненныъх задач")
    
    def mark_done(title: str):
        for task in tasks:
            if task.title.upper() == title.upper():
                task.completed = True
                return
            
        raise TaskNotFoundError("Такой задачи не существует")
    
    def delete_task(title: str):
        for i, task in enumerate(tasks):
            if task.title.upper() == title.upper():
                del tasks[i]
                return
        raise TaskNotFoundError("Такой задачи не существует")
        
    
    return add_task, show_all, show_pending, mark_done, delete_task