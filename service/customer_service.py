import re
import utility.helpers
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError
from utility.helpers import validate_name, check_date, validate_email, validate_postal_code


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customers_objects = self.customer_dao.get_all_customers()

        return list(map(lambda x: x.to_dict(), list_of_customers_objects))

    def get_customer_by_id(self, customer_id):
        cust = self.customer_dao.get_customer_by_id(customer_id)

        if not cust:
            raise CustomerNotFoundError(f"The requested customer ID:"
                                        f" {customer_id} was not found")

        return cust.to_dict()

    def add_customer(self, cust):
        reg_phone = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"

        if not validate_name(cust.get_first_name()) or not validate_name(cust.get_last_name()):
            pass
        if check_date(cust.get_date_of_birth()):
            pass
        if validate_email(cust.get_email()):
            pass
        if validate_postal_code(cust.get_postal_code()):
            pass
        elif not re.match(reg_phone, cust.get_mobile_phone()):
            raise InvalidParameterError("mobile phone format 555-555-5555")

        return self.customer_dao.add_customer(cust).to_dict()

    def update_customer_by_id(self, cust):
        pass



