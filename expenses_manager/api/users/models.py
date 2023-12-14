from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return {self.id, self.nickname}
