class Task:
    def __init__(self, description, completed, ID):
        self.description = description
        self.completed = completed
        self.ID = ID

    def __str__(self):
        return f'{self.description} "(Done!)"'


# task = Task("h", 0, 0)

# print(task)
