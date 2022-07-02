from dao.customer_dao import CustomerDao
from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFound
from exception.unauthorized_access import UnauthorizedAccess
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
        args = validate_args(args)
        res = []
        for acc in self.account_dao.get_accounts_by_customer_id(customer_id, args):
            res.append(acc.to_dict())
        return res

    def get_customer_account_by_account_id(self, customer_id, account_id):
        #  4 paths, account not found, customer not found, account not associated with customer and retrieve account
        account = self.account_dao.get_account_by_id(account_id)
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"The requested customer ID:{customer_id} was not found")
        if not account:
            raise AccountNotFound(f"The requested account ID:{account_id} was not found")
        if not self.account_dao.get_customer_account_by_account_id(customer_id, account_id):
            raise UnauthorizedAccess(f"The requested account ID:"
                                     f"{account_id} is not associated with the provided customer ID:{customer_id}")
        else:
            return account.to_dict()

    def update_customer_account_by_account_id(self, customer_id, account_id):
        updated_account = self.account_dao.update_account_by_id(account_id)
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"The requested customer ID:{customer_id} was not found")
        if not self.account_dao.get_account_by_id(account_id):
            raise AccountNotFound(f"The requested account ID:{account_id} was not found")
        if not self.account_dao.get_customer_account_by_account_id(customer_id, account_id):
            raise UnauthorizedAccess(f"The requested account ID:"
                                     f"{account_id} is not associated with the provided customer ID:{customer_id}")
        else:
            return updated_account.to_dict()
