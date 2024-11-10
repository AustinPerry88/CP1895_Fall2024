import sqlite3

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()

# Check if the Task table exists and view its structure
cursor.execute("PRAGMA table_info(Task)")
print(cursor.fetchall())

# Check if there are any rows in the Task table
cursor.execute("SELECT * FROM Task")
print(cursor.fetchall())

conn.close()
