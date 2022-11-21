from sqlitedb import *
from main import *
from sqlitedb import *


def command_menu():
    print(
        """\nCOMMAND MENU
view          - View pending tasks
history       - View completed tasks
add           - Add a task
complete      - Complete a task
delete        - Delete a task
exit          - Exit the program"""
    )


def main():
    print("Task List\n")

    command_menu()
    command = input("\nCommand: ").lower()
    while command != "exit":
        if command == "view":
            view_task()
        elif command == "history":
            history_task()
        elif command == "add":
            description = input("Description: ")
            task = Task(description, 0, None)
            add_task(task)
        elif command == "complete":
            number = input("Task number to complete: ")
            complete_task(number)
        elif command == "delete":
            number = input("Task number to delete: ")
            delete_task(number)
            conn.close()
        command = input("\nCommand: ").lower()
    print("Bye!")
    exit()


main()
