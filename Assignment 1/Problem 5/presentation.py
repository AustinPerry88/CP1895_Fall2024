import business

def display_menu():
    print("\nCOMMAND MENU")
    print("view     - View pending tasks")
    print("history  - View completed tasks")
    print("add      - Add a task")
    print("complete - Complete a task")
    print("delete   - Delete a task")
    print("exit     - Exit program")

def display_tasks(tasks, completed=False):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            task_id, description = task
            status = " (DONE!)" if completed else ""
            print(f"{task_id}. {description}{status}")

def main():
    business.initialize_database()

    while True:
        display_menu()
        command = input("\nCommand: ").strip().lower()
        print()

        if command == "view":
            tasks = business.view_pending_tasks()
            display_tasks(tasks)

        elif command == "history":
            tasks = business.view_completed_tasks()
            display_tasks(tasks, completed=True)

        elif command == "add":
            description = input("Description: ").strip()
            business.add_new_task(description)
            print(f"Task '{description}' added.")

        elif command == "complete":
            tasks = business.view_pending_tasks()
            display_tasks(tasks)
            if tasks:
                task_id = input("Number: ").strip()
                is_valid, message = business.validate_task_id(task_id, tasks)
                if is_valid:
                    business.mark_task_as_completed(int(task_id))
                    print(f"Task {task_id} marked as completed.")
                else:
                    print(message)

        elif command == "delete":
            tasks = business.view_pending_tasks()
            display_tasks(tasks)
            if tasks:
                task_id = input("Number: ").strip()
                is_valid, message = business.validate_task_id(task_id, tasks)
                if is_valid:
                    business.delete_task(int(task_id))
                    print(f"Task {task_id} deleted.")
                else:
                    print(message)

        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
