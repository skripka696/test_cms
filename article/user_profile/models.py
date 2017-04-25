from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('editor', 'editor'),
        ('author', 'author'),
        ('reader', 'reader')
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='reader')
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.username
