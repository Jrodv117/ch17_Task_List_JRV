from sqlitedb import *
from main import *

# task1 = Task("Walk Harlee", 0, None)

# taskk = add_task(task1)

# taskk = delete_task(task1)

taskk1 = view_task(0)
print(taskk1)
conn.close()
