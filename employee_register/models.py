from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete= models.CASCADE)


class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    username=None

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

