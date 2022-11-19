import sqlite3
from main import *

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()

task1 = Task("Walk Harlee", 0, None)


def view_task(not_completed):
    with conn:
        cursor.execute(
            "SELECT * FROM Task WHERE completed=:completed",
            {"completed": not_completed},
        )
        return cursor.fetchall()


def history_task(completed_task):
    with conn:
        cursor.execute(
            "SELECT * FROM Task WHERE completed=:completed",
            {"completed": completed_task},
        )
        return cursor.fetchall()


def add_task(task_object):
    with conn:
        cursor.execute(
            "INSERT INTO Task VALUES (:ID, :description, :completed)",
            {
                "ID": task_object.ID,
                "description": task_object.description,
                "completed": task_object.completed,
            },
        )


def complete_task():
    pass


def delete_task(task_object):
    with conn:
        cursor.execute(
            "DELETE from Task WHERE description = :description",
            {"description": task_object.description},
        )
