from dao.customer_dao import CustomerDao
from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFound
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
            raise CustomerNotFound(f"The requested customer ID: {customer_id} was not found")
        return self.account_dao.add_account_by_customer_id(account, customer_id).to_dict()

    def get_accounts_by_customer_id(self, customer_id, args):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFound(f"The requested customer ID:"
                                   f" {customer_id} was not found")
        filtered_accounts_list = []
        if validate_args(args):
            args_length = len(args)

            if args_length == 2:
                amount_greater_than = args['amountGreaterThan']

                amount_less_than = args['amountLessThan']
                filtered_accounts_list = self.account_dao.get_accounts_by_customer_id_agt_alt(customer_id,
                                                                                              amount_greater_than,
                                                                                              amount_less_than)
            elif args_length == 1:
                if 'amountGreaterThan' in args.keys():
                    amount_greater_than = args['amountGreaterThan']
                    filtered_accounts_list = self.account_dao.get_accounts_by_customer_id_agt(customer_id,
                                                                                              amount_greater_than)
                else:
                    amount_less_than = args['amountLessThan']
                    filtered_accounts_list = self.account_dao.get_accounts_by_customer_id_alt(customer_id,
                                                                                              amount_less_than)
        else:
            filtered_accounts_list = self.account_dao.get_accounts_by_customer_id(customer_id)

        result = []
        for acc in filtered_accounts_list:
            result.append(acc.to_dict())
        return result

    def get_customer_account_by_account_id(self, customer_id, account_id):
        #  4 paths, account not found, customer not found, account not associated with customer and retrieve account
        account = self.account_dao.get_account_by_id(account_id)
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFound(f"The requested customer ID:{customer_id} was not found")
        if not account:
            raise AccountNotFound(f"The requested account ID:{account_id} was not found")
        if not self.account_dao.get_customer_account_by_account_id(customer_id, account_id):
            raise UnauthorizedAccess(f"The requested account ID:"
                                     f"{account_id} is not associated with the provided customer ID:{customer_id}")
        return self.account_dao.get_customer_account_by_account_id(customer_id, account_id).to_dict()

    def update_customer_account_by_account_id(self, customer_id, account):
        updated_account = self.account_dao.update_account_by_id(account)
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFound(f"The requested customer ID:{customer_id} was not found")
        if not self.account_dao.get_account_by_id(account.get_account_id()):
            raise AccountNotFound(f"The requested account ID:{account.get_account_id()} was not found")
        if not self.account_dao.get_customer_account_by_account_id(customer_id, account.get_account_id()):
            raise UnauthorizedAccess(f"The requested account ID:"
                                     f"{account.get_account_id()} is not associated with the provided customer ID:{customer_id}")
        else:
            return updated_account.to_dict()

    def delete_customer_account_by_account_id(self, customer_id, account_id):

        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFound(f"The requested customer ID:{customer_id} was not found")
        if not self.account_dao.get_account_by_id(account_id):
            raise AccountNotFound(f"The requested account ID:{account_id} was not found")
        if not self.account_dao.get_customer_account_by_account_id(customer_id, account_id):
            raise UnauthorizedAccess(f"The requested account ID:"
                                     f"{account_id} is not associated with the provided customer ID:{customer_id}")
        else:
            if self.account_dao.check_for_joined_accounts_by_id(account_id) is None:
                return {"message": f"Customer account with ID: {account_id} is not associated with any customers"}
            elif self.account_dao.check_for_joined_accounts_by_id(account_id):
                assoc = self.account_dao.delete_joined_association(account_id, customer_id)
                return {"message": f"Customer account with ID: {assoc[0]} cannot be deleted because customer "
                                   f"with ID: {assoc[1]} is not the only account owner, however this "
                                   f"customer is no longer associated with this account"}
            else:
                self.account_dao.delete_joined_association(account_id, customer_id)
                self.account_dao.delete_account_by_id(account_id)
            return {"message": f"Customer account with ID: {account_id} and its associations were "
                               f"successfully deleted!"}
