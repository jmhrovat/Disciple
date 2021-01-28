from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", unique=True)

    def __str__(self):
        return self.user.last_name + ', ' + self.user.first_name


    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_profile, sender=User)

    def update_profile(sender, instance, created, **kwargs):

        if created == False:
            instance.profile.save()

    post_save.connect(update_profile, sender=User)

