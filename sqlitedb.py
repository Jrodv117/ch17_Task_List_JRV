import sqlite3
from main import *

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()

task1 = Task("Walk Harlee", 0, None)

cursor.execute(
    "INSERT INTO Task VALUES (:description, :completed, :ID)",
    {"description": task1.description, "completed": task1.completed, "ID": task1.ID},
)

conn.commit()
conn.close()
