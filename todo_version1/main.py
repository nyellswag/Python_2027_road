from todo import TodoManager, Task, TaskFeatures, TaskStatus, TaskNotFoundError

if __name__ == "__main__":
    manager = TodoManager()

    print("\n--- 1. Пустой список ---")
    try:
        print(list(manager.show_all()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 2. Добавление обычной задачи ---")
    try:
        manager.add_task("Купить молоко")
        print("Обычная задача добавлена")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 3. Добавление срочной задачи ---")
    try:
        manager.add_task("Сдать проект", deadline=2)
        print("Срочная задача добавлена")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 4. Добавление задачи с тегами ---")
    try:
        manager.add_task("Подготовить конспект", tags=["study", "python"])
        print("Задача с тегами добавлена")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 5. Показать все задачи ---")
    try:
        print(list(manager.show_all()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 6. Показать невыполненные задачи ---")
    try:
        print(list(manager.show_pending()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 7. Отметить задачу как выполненную ---")
    try:
        manager.mark_done("Купить молоко")
        print("Задача отмечена как выполненная")
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 8. После mark_done ---")
    try:
        print(list(manager.show_all()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 9. Удаление задачи ---")
    try:
        manager.delete_task("Подготовить конспект")
        print("Задача удалена")
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n--- 10. После удаления ---")
    try:
        print(list(manager.show_all()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 11. Удаление несуществующей задачи ---")
    try:
        manager.delete_task("Несуществующая задача")
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n--- 12. Проверка срочных задач ---")
    try:
        print(list(manager.storage.get_urgent_tasks()))
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 13. Проверка validate_title: пустая строка ---")
    try:
        manager.add_task("   ")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 14. Проверка validate_title: короткая строка ---")
    try:
        manager.add_task("Hi")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 15. Проверка from_list ---")
    try:
        data = ["Задача 1", "Задача 2", "Задача 3"]
        new_manager = TodoManager.from_list(data)
        print(list(new_manager.show_all()))
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 16. Количество созданных менеджеров ---")
    print(TodoManager.total_managers_created)

    print("\n--- 17. Проверка __len__ storage ---")
    print(len(manager.storage))

    print("\n--- 18. Проверка __getitem__ storage ---")
    try:
        print(manager.storage[0])
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 19. Проверка __iter__ storage ---")
    try:
        for task in manager.storage:
            print(task)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 20. Проверка свойств первой задачи ---")
    try:
        first_task = manager.storage[0]
        print("title:", first_task.title)
        print("completed:", first_task.completed)
        print("display_info:", first_task.display_info)
        print("is_urgent:", first_task.is_urgent)
        print("repr:", repr(first_task))
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 21. Проверка features срочной задачи ---")
    try:
        urgent_task = manager.storage.find_by_title("Сдать проект")
        print("title:", urgent_task.title)
        print("deadline:", urgent_task.features.deadline)
        print("priority:", urgent_task.features.priority)
        print("tags:", urgent_task.features.tags)
        print("is_urgent:", urgent_task.is_urgent)
    except Exception as e:
        print(f"Ошибка: {e}")