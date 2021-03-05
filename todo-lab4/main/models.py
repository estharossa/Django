from django.db import models


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
