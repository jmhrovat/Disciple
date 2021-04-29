from django.db import models
from users.models import Profile
from django.contrib.auth.models import User



# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 200)
    profiles = models.ManyToManyField(User, through='TaskStatus')


    def __str__(self):
        return self.name

class TaskStatus(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)




