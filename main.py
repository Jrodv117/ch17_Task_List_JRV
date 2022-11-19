class Task:
    def __init__(self, description, completed, taskid):
        self.description = description
        self.completed = completed
        self.taskid = taskid

    def __str__(self):
        return f'{self.description} "(Done!)"'
