from utils import print_tasks
from todo import create_todo_manager

if __name__ == '__main__':
    add, show_all, show_pending, mark_done, delete = create_todo_manager()

    print('--Проверка Добавления--')
    try:
        add('Сделать Python')
        add('Сделать Web')
        add('Созвониться с друзьями')
        print('Задачи добавлены')
    except ValueError as e:
        print(f'Ошибка: {e}')

    print("--Добавление пустой строки--")
    try:
        add('')
    except ValueError as e:
        print(f'Ошибка: {e}')

    print("--Показ всего листа--")
    try:
        print_tasks(show_all())
    except ValueError as e:
        print(f'Ошибка: {e}')

    print("--Только невыполненные задачи--")
    try:
        print_tasks(show_pending())
    except ValueError as e:
        print(f'Ошибка: {e}')

    print("--Проверка отметки--")
    try:
        mark_done('СоЗвониться с ДРУЗЬЯМИ')
        print('Задача отмечена как выполненная')
    except Exception as e:
        print(f'Ошибка: {e}')

    print("--Проверка удаления--")
    try:
        delete('СделАть WeB')
        print('Задача удалена')
    except Exception as e:
        print(f'Ошибка: {e}')

    print("--Список задач--")
    try:
        print_tasks(show_all())
    except ValueError as e:
        print(f'Ошибка: {e}')

    print("--Только невыполненные после изменений--")
    try:
        print_tasks(show_pending())
    except ValueError as e:
        print(f'Ошибка: {e}')