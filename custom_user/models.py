from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(
        upload_to="user_profile_image/%Y/%m/%d", null=True, blank=True
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Phone"
    )
