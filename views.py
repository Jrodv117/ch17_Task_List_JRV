from sqlitedb import *
from main import *

task1 = Task("Walk Harlee", 0, None)

taskk = add_task(task1)

taskk = delete_task(task1)
conn.close()
