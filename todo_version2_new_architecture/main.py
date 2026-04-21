from todo import TodoManager, Task, TaskFeatures


def print_block(title):
    print(f"\n--- {title} ---")


if __name__ == "__main__":
    manager = TodoManager()

    print_block("1. Пустой список")
    try:
        print(list(manager.show_all()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("2. Добавление обычной задачи")
    try:
        manager.add_task("Купить молоко")
        print("Обычная задача добавлена")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("3. Добавление срочной задачи")
    try:
        manager.add_task("Сдать проект", deadline=2, priority="urgent")
        print("Срочная задача добавлена")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("4. Добавление задачи с тегами")
    try:
        manager.add_task("Подготовить конспект", tags=["study", "python"])
        print("Задача с тегами добавлена")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("5. Показать все задачи")
    try:
        for task in manager.show_all():
            print(task.display_info if hasattr(task, "display_info") else task)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("6. Показать невыполненные задачи")
    try:
        for task in manager.show_pending():
            print(task.display_info if hasattr(task, "display_info") else task)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("7. Показать срочные задачи")
    try:
        for task in manager.show_urgent_tasks():
            print(task.display_info if hasattr(task, "display_info") else task)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("8. Использование свойств первой задачи")
    try:
        first_task = manager.storage[0]
        print("display_info:", first_task.display_info)
        print("is_urgent:", first_task.is_urgent)
        print("is_completed:", first_task.is_completed)
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("9. Перебор через for task in manager.storage")
    try:
        for task in manager.storage:
            print(task.display_info)
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("10. Доступ по индексу manager.storage[0]")
    try:
        print(manager.storage[0].display_info)
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("11. Проверка len(manager.storage)")
    try:
        print(len(manager.storage))
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("12. Отметить задачу как выполненную")
    try:
        manager.mark_done("Купить молоко")
        print(manager.storage.find_by_title("Купить молоко").display_info)
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("13. Удаление задачи")
    try:
        manager.delete_task("Подготовить конспект")
        for task in manager.show_all():
            print(task.display_info if hasattr(task, "display_info") else task)
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("14. Добавление готового объекта Task напрямую в storage")
    try:
        custom_task = Task(
            title="Готовый объект Task",
            features=TaskFeatures(deadline=1, priority="urgent", tags=["custom"])
        )
        manager.storage.add(custom_task)
        print(manager.storage.find_by_title("Готовый объект Task").display_info)
    except Exception as e:
        print(f"Ошибка: {e}")

    print_block("15. Обработка ошибок: пустой title")
    try:
        manager.add_task("   ")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("16. Обработка ошибок: короткий title")
    try:
        manager.add_task("Hi")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("17. Обработка ошибок: удалить несуществующую задачу")
    try:
        manager.delete_task("Не существует")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("18. Обработка ошибок: найти несуществующую задачу")
    try:
        print(manager.storage.find_by_title("Нет такой задачи"))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_block("19. Количество созданных менеджеров")
    try:
        print(TodoManager.total_managers)
    except Exception as e:
        print(f"Ошибка: {e}")
