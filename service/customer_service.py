from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError


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
