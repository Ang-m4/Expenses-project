from rest_framework.exceptions import NotFound
from api.expenses.models import Expense
from api.expenses.serializer import ExpenseSerializer


class ExpenseService():

    def get_expense_by_id(self, expense_id):
        expense = Expense.objects.get(id=expense_id)
        if expense:
            serializer = ExpenseSerializer(expense)
            serializer.is_valid(raise_exception=True)
            return serializer.data
        else:
            raise NotFound("Expense not found")

    def get_user_expenses(self, owner_id):
        expenses = Expense.objects.filter(owner__id=owner_id)
        if expenses:
            serializer = ExpenseSerializer(expenses, many=True)
            serializer.is_valid(raise_exception=True)
            return serializer.data
        else:
            raise NotFound("Expenses not found for the selected user")

    def add_new_expense(self, expense, owner_id):
        serializer = ExpenseSerializer(data=expense)
        serializer.is_valid(raise_exception=True)
        new_expense = serializer.save(owner_id=owner_id)
        return new_expense

    def delete_user_expense(self, expense_id):
        pass

    def update_expense(self, expense_id, expense):
        pass

    def get_expenses_by_category(self, category_id):
        pass

    def get_expenses_by_date(self, date):
        pass

    def get_expenses_by_date_range(self, start_date, end_date):
        pass

    def get_expenses_by_category_and_date_range(self, category_id, start_date, end_date):
        pass
        