from django.db import models
from api.categories.models import Category
from api.users.models import User


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    date = models.DateField()
    description = models.CharField(max_length=100)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return {self.amount, self.date, self.description, self.category}
