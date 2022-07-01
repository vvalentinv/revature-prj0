from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from utility.helpers import validate_name, check_date, validate_email, \
    validate_postal_code, validate_phone


class AccountService:

    def add_account_by_customer_id(self, account, customer_id):
        cust = self.customer_dao.get_customer_by_id(customer_id)
        if not cust:
            raise CustomerNotFoundError(f"The requested customer ID:"
                                        f" {customer_id} was not found")
            return self.account_dao.add_account_by_customer_id(self, account, customer_id).to_dict()

