import sqlite3
from main import *

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()

task1 = Task("Walk Harlee", 0, None)


def create_task(task_object):
    with conn:
        cursor.execute(
            "INSERT INTO Task VALUES (:ID, :description, :completed)",
            {
                "ID": task_object.ID,
                "description": task_object.description,
                "completed": task_object.completed,
            },
        )


def read_task():
    pass


def update_task():
    pass


def delete_task():
    pass
