from dao.customer_dao import CustomerDao
from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from utility.helpers import validate_name, check_date, validate_email, \
    validate_postal_code, validate_phone, validate_args


class AccountService:

    def __init__(self):
        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def add_account_by_customer_id(self, account, customer_id):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"The requested customer ID:"
                                        f" {customer_id} was not found")
        return self.account_dao.add_account_by_customer_id(account, customer_id).to_dict()

    def get_accounts_by_customer_id(self, customer_id, args):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"The requested customer ID:"
                                        f" {customer_id} was not found")
        validate_args(args)
        return self.account_dao.get_accounts_by_customer_id(customer_id, args).to_dict()
