import sqlite3
from main import *

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()


conn.execute(
    "CREATE TABLE Task(description TEXT NOT NULL, completed INTEGER NOT NULL,taskID INTEGER PRIMARY KEY AUTOINCREMENT);"
)

conn.execute(
    """INSERT INTO Task (description, completed) Values
    ('Get Bike Fixed', 1),
    ('Call your mom',1),
    ('Buy toothbrush',0),
    ('Do homework',0);"""
)

task1 = Task("Walk Harlee", 0, None)
# task1 = Task("Feed Harlee", 0, None)
cursor.execute(
    # "INSERT INTO Task VALUES (?,?,?)",
    # (task1.description, task1.completed, task1.taskid),
    "INSERT INTO Task VALUES (:description, :completed, :ID)",
    {
        "description": task1.description,
        "completed": task1.completed,
        "ID": task1.taskid,
    },
)

conn.commit()
conn.close()
