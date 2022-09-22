from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    login_id = models.TextField(unique=True)
    email = models.EmailField()

    # def __str__(self):
    #     return self.user
