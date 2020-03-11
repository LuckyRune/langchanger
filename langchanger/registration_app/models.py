from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_icon = models.ImageField()
    description = models.TextField()
    rate = models.PositiveIntegerField()
    achievements = models.ManyToManyField("Achievements")


class Achievements(models.Model):
    name = models.TextField()
    rate = models.PositiveIntegerField()

    def add_rate(self, user: UserProfile):
        user.rate += self.rate
