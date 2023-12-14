from api.expenses.models import Expense


class ExpenseService():

    def get_expense_by_id(self, expense_id):
        pass

    def get_user_expenses(self, owner_id):
        pass

    def add_new_expense(self, expense, owner_id):
        pass

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

    