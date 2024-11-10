import sqlite3

DATABASE_FILE = "task_list_db.sqlite"

def create_connection():
    return sqlite3.connect(DATABASE_FILE)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Task (
                        taskID INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        completed INTEGER DEFAULT 0
                      )''')
    conn.commit()
    conn.close()

def get_pending_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT taskID, description FROM Task WHERE completed = 0")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def get_completed_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT taskID, description FROM Task WHERE completed = 1")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Task (description, completed) VALUES (?, 0)", (description,))
    conn.commit()
    conn.close()

def complete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Task SET completed = 1 WHERE taskID = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Task WHERE taskID = ?", (task_id,))
    conn.commit()
    conn.close()
