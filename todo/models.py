from django.db import models


# Create your models here.

class Todo(models.Model):
    PRIORITIES = [
        (1, 'NOT VERY IMPORTANT'),
        (2, 'NORMAL'),
        (3, 'URGENT'),
    ]
    TYPES = ('daily', 'weekly', 'monthly', 'yearly')
    title = models.CharField(max_length=255)
    priority = models.IntegerField(choices=PRIORITIES, default=2)
    type = models.CharField(choices=TYPES, default=TYPES.index(0))
    # repeat = models.BooleanField(default=False)
    dueDateTime = models.DateTimeField()
    done = models.BooleanField(default=False)
