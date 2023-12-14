from rest_framework import serializers
from api.categories.models import Category
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'description', 'category']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

    def validate_category(self, value):
        if Category.objects.filter(id=value.id).exists():
            return value
        raise serializers.ValidationError("Category does not exist")
