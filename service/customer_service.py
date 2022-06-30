import re
import utility.helpers
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError


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
        reg_email = r"[^@]+@[^@]+\.[^@]+"
        if len(cust.get_first_name()) < 2 or len(cust.get_last_name()) < 2:
            raise InvalidParameterError("Names must have at least 2 letters")
        elif " " in cust.get_first_name() or " " in cust.get_last_name():
            raise InvalidParameterError("Username cannot contain spaces")
        elif not utility.helpers.check_date(cust.get_date_of_birth()):
            raise InvalidParameterError("Minimum Customer age must be 16 years-old")
        elif not re.match(reg_email, cust.get_email()):
            raise InvalidParameterError("accepted email address format is <username>@<company>.<domain>")
        elif not 4 < len(cust.get_postal_code()) < 7:
            raise InvalidParameterError("Postal code length must be equal to 5 or 6")
        elif not re.match(reg_phone, cust.get_mobile_phone()):
            raise InvalidParameterError("mobile phone format 555-555-5555")

        return self.customer_dao.add_customer(cust).to_dict()

