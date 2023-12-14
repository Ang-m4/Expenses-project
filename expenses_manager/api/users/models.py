from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    def __str__(self):
        return {self.id, self.nickname}
