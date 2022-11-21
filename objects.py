class Task:
    def __init__(self, description, completed, ID=None):
        self.description = description
        self.completed = completed
        self.ID = ID

    def __str__(self):
        return f'{self.description} "(Done!)"'
