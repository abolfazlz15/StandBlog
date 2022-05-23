from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=25)
    mlicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profile/images")

    def __str__(self):
        return self.user.username
