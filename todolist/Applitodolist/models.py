from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 20)
    is_completed = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add = True)
    finish_date = models.DateTimeField(null = True, blank = True)

    priority_choices = [
        ('low','Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    priority = models.CharField(max_length = 10, choices = priority_choices, default = 'medium')
    def __str__(self):
        return self.title

