from dao.customer_dao import CustomerDao


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customers_objects = self.customer_dao.get_all_customers()

        return list(map(lambda x: x.to_dict(), list_of_customers_objects))
