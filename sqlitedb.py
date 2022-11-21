import sqlite3
from main import *

conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()


def view_task():
    with conn:
        query = cursor.execute(
            "SELECT * FROM Task WHERE completed=0",
        )
        for row in query:
            print(row[0], row[1])


def history_task():
    with conn:
        query = cursor.execute(
            "SELECT * FROM Task WHERE completed=1",
        )
        for row in query:
            print(row[0], row[1], "(DONE!)")


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


def complete_task(task_number):
    with conn:
        cursor.execute(
            "UPDATE Task SET completed = 0 WHERE taskID=:taskID",
            {"taskID": task_number},
        )
        return cursor.fetchall()


def delete_task(task_number):
    with conn:
        cursor.execute(
            "DELETE from Task WHERE taskID=:taskID",
            {"taskID": task_number},
        )
