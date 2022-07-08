from dao.customer_dao import CustomerDao
from dao.account_dao import AccountDao
from exception.customer_not_found import CustomerNotFound
from utility.helpers import validate_name, check_date, validate_email, \
    validate_postal_code, validate_phone


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()
        self.account_dao = AccountDao()

    def get_all_customers(self):
        list_of_customers_objects = self.customer_dao.get_all_customers()

        return list(map(lambda x: x.to_dict(), list_of_customers_objects))

    def get_customer_by_id(self, customer_id):
        cust = self.customer_dao.get_customer_by_id(customer_id)

        if not cust:
            raise CustomerNotFound(f"The requested customer ID:"
                                   f" {customer_id} was not found")

        return cust.to_dict()

    def add_customer(self, cust):
        if validate_name(cust.get_first_name()) and validate_name(cust.get_last_name()) and \
                check_date(cust.get_date_of_birth()) and validate_email(cust.get_email()) \
                and validate_postal_code(cust.get_postal_code()) and validate_phone(cust.get_mobile_phone()):
            return self.customer_dao.add_customer(cust).to_dict()

    def update_customer_by_id(self, cust):
        if not self.customer_dao.get_customer_by_id(cust.get_customer_id()):
            raise CustomerNotFound(f"Customer with id {cust.get_customer_id()} was not found")
        if validate_name(cust.get_first_name()) and validate_name(cust.get_last_name()) and \
                check_date(cust.get_date_of_birth()) and validate_email(cust.get_email()) \
                and validate_postal_code(cust.get_postal_code()) and validate_phone(cust.get_mobile_phone()):
            if self.customer_dao.update_customer_by_id(cust):
                return self.customer_dao.update_customer_by_id(cust).to_dict()

    def delete_customer_by_id(self, customer_id):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFound(f"The requested customer ID:"
                                   f" {customer_id} was not found")

        owned_accounts = self.account_dao.get_accounts_by_customer_id(customer_id)
        if owned_accounts:

            for acc in owned_accounts:
                has_joined_accounts = self.account_dao.check_for_joined_accounts_by_id(acc.get_account_id())

                if has_joined_accounts:
                    self.account_dao.delete_joined_association(acc.get_account_id(), customer_id)
                else:
                    self.account_dao.delete_joined_association(acc.get_account_id(), customer_id)
                    self.account_dao.delete_account_by_id(acc.get_account_id())

        return self.customer_dao.delete_customer_by_id(customer_id)
