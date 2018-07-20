from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()