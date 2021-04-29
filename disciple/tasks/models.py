from django.db import models
from users.models import Profile

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 200)
    profiles = models.ManyToManyField(Profile, through='TaskStatus')


    def __str__(self):
        return self.name

class TaskStatus(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)




