from rest_framework import serializers
from rest_framework.exceptions import NotFound
from api.users.models import User
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
    
    def create(validated_data, owner_id):
        owner = User.objects.get(id=owner_id)
        if not owner:
            raise NotFound("Owner not found")
        category = Category.objects.create(owner=owner, **validated_data)
        return category
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        return instance