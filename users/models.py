from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


# Create your models here.
class Researcher(models.Model):
    username = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email_address', max_length=255, unique=True)
    date_of_birth = models.CharField(blank=True, max_length=150)
    department = models.CharField(default="", blank=True, null=True, max_length=350)
    bio = models.CharField(default="", blank=True, null=True, max_length=350)
    profile_picture = models.ImageField(upload_to='Profile Pictures', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email