from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)

    followings = models.ManyToManyField('self', related_name='following', blank=True, symmetrical=False)
    followers = models.ManyToManyField('self', related_name='follower', blank=True, symmetrical=False)


    

# class UserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
#     follows = models.ManyToManyField('self', blank=True, related_name='profile')
#     followers = models.ManyToManyField('self', blank=True)

#     def __str__(self) -> str:
#         return f'{self.user.username} - Profile'