from todo import TodoManager, TaskNotFoundError

if __name__ == "__main__":
    manager = TodoManager()

    print("\n--- 1. Проверка пустого списка ---")
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

    print("\n--- 3. Добавление срочной задачи с дедлайном ---")
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

    print("\n--- 7. Проверка поиска и отметки задачи как выполненной ---")
    try:
        manager.mark_done("Купить молоко")
        print("Задача отмечена как выполненная")
        print(list(manager.show_all()))
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n--- 8. Проверка удаления задачи ---")
    try:
        manager.delete_task("Подготовить конспект")
        print("Задача удалена")
        print(list(manager.show_all()))
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n--- 9. Попытка удалить несуществующую задачу ---")
    try:
        manager.delete_task("Несуществующая задача")
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n--- 10. Попытка отметить несуществующую задачу как выполненную ---")
    try:
        manager.mark_done("Несуществующая задача")
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n--- 11. Проверка срочных задач через storage ---")
    try:
        print(list(manager.storage.get_urgent_tasks()))
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 12. Проверка validate_title: пустая строка ---")
    try:
        manager.add_task("   ")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 13. Проверка validate_title: слишком короткая строка ---")
    try:
        manager.add_task("Hi")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 14. Проверка from_list ---")
    try:
        tasks_data = ["Задача 1", "Задача 2", "Задача 3"]
        new_manager = TodoManager.from_list(tasks_data)
        print("Создан новый менеджер из списка:")
        print(list(new_manager.show_all()))
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 15. Проверка количества созданных менеджеров ---")
    try:
        print(f"Всего создано менеджеров: {TodoManager.total_managers_created}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 16. Проверка __len__ у storage ---")
    try:
        print(f"Количество задач в storage: {len(manager.storage)}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 17. Проверка __getitem__ у storage ---")
    try:
        print("Первая задача через storage[0]:")
        print(manager.storage[0])
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 18. Проверка __iter__ у storage ---")
    try:
        print("Перебор всех задач через for task in manager.storage:")
        for task in manager.storage:
            print(task)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 19. Проверка repr у первой задачи ---")
    try:
        print(repr(manager.storage[0]))
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- 20. Проверка features у срочной задачи ---")
    try:
        urgent_task = manager.storage.find_by_title("Сдать проект")
        print("Title:", urgent_task.title)
        print("Deadline:", urgent_task.features.deadline)
        print("Priority:", urgent_task.features.priority)
        print("Tags:", urgent_task.features.tags)
        print("Is urgent:", urgent_task.is_urgent())
    except Exception as e:
        print(f"Ошибка: {e}")