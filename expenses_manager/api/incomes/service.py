from api.incomes.models import Income


class IncomeService():

    def get_income_by_id(self, income_id):
        pass

    def get_user_incomes(self, owner_id):
        pass

    def add_new_income(self, income, owner_id):
        pass

    def delete_user_income(self, income_id):
        pass

    def update_income(self, income_id, income):
        pass

    def get_incomes_by_category(self, category_id):
        pass

    def get_incomes_by_date(self, date):
        pass

    def get_incomes_by_date_range(self, start_date, end_date):
        pass

    def get_incomes_by_category_and_date_range(self, category_id, start_date, end_date):
        pass
