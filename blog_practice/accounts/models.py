from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    phone = PhoneNumberField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email