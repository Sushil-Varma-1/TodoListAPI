from django.db import models


# Create a Model
class TodoListModel(models.Model):
    statusChoices = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue')
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField(blank=True)
    status = models.CharField(max_length=8, choices=statusChoices, default='OPEN')
    tags = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.title
