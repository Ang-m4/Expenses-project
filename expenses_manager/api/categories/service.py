from api.categories.serializer import CategorySerializer
from api.categories.models import Category
from api.users.models import User
from rest_framework.exceptions import NotFound


class CategoryService():

    def get_category_by_id(self, category_id):
        category = Category.objects.get(id=category_id)
        if category:
            serializer = CategorySerializer(category)
            serializer.is_valid(raise_exception=True)
            return serializer.data
        else:
            raise NotFound("Category not found")

    def get_user_categories(self, owner_id):
        categories = Category.objects.filter(owner__id=owner_id)
        if categories:
            serializer = CategorySerializer(categories, many=True)
            serializer.is_valid(raise_exception=True)
            return serializer.data
        else:
            raise NotFound("Categories not found for the selected user")

    def add_new_category(self, category, owner_id):
        serializer = CategorySerializer(data=category)
        serializer.is_valid(raise_exception=True)
        new_category = serializer.save(owner_id=owner_id)
        return new_category

    def delete_user_category(self, category_id):
        #Todo - Validate if the user is the user owns the category
        category = Category.objects.get(id=category_id)
        if category:
            category.delete()
        else:
            raise NotFound("Category not found")

    def update_category(self, category_id, category):
        #Todo - Validate if the user is the user owns the category
        category_to_update = Category.objects.get(id=category_id)
        if category_to_update:
            serializer = CategorySerializer(category_to_update, data=category)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data
        else:
            raise NotFound("Category not found")
