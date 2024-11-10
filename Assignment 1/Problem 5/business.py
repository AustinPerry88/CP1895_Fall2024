import database

def initialize_database():
    database.create_table()

def view_pending_tasks():
    return database.get_pending_tasks()

def view_completed_tasks():
    return database.get_completed_tasks()

def add_new_task(description):
    if description:
        database.add_task(description)
    else:
        print("Task description cannot be empty.")

def mark_task_as_completed(task_id):
    database.complete_task(task_id)

def delete_task(task_id):
    database.delete_task(task_id)

def validate_task_id(task_id, tasks):
    if task_id.isdigit():
        task_id = int(task_id)
        if any(task[0] == task_id for task in tasks):
            return True, ""
        else:
            return False, "Error: Task ID not found."
    else:
        return False, "Error: Please enter a valid task number."
