from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFound
from utility.helpers import validate_name, check_date, validate_email, \
    validate_postal_code, validate_phone


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

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
        if not validate_name(cust.get_last_name()):
            pass
        if validate_email(cust.get_email()):
            pass
        if validate_postal_code(cust.get_postal_code()):
            pass
        if validate_phone(cust.get_mobile_phone()):
            pass

        updated_customer = self.customer_dao.update_customer_by_id(cust)
        if updated_customer is None:
            raise CustomerNotFound(f"Customer with id {cust.get_customer_id()} was not found")

        return updated_customer.to_dict()

    def delete_customer_by_id(self, customer_id):
        #  -here goes code to find, check account balance and call Dao layer delete account func???(business logic)
        confirmed_deletion = self.customer_dao.delete_customer_by_id(customer_id)
        if confirmed_deletion is None:
            raise CustomerNotFound(f"Customer with id: {customer_id} was not found")
        return confirmed_deletion
