import sqlite3
from main import *

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()

task1 = Task("Walk Harlee", 0, None)

# def create_task(task_object)
#     withc conn:

cursor.execute(
    "INSERT INTO Task VALUES (:ID, :description, :completed)",
    {
        "ID": task1.ID,
        "description": task1.description,
        "completed": task1.completed,
    },
)

conn.commit()
conn.close()
