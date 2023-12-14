from rest_framework import serializers
from api.categories.models import Category
from api.users.models import User
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
    
    def create(self, validated_data, owner_id):
        owner = User.objects.get(id=owner_id)
        if not owner:
            raise serializers.ValidationError("User does not exist")
        expense = Expense.objects.create(owner=owner, **validated_data)
        return expense
    