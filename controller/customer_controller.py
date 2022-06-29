from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService

cc = Blueprint('customer_controller', __name__)
customer_service = CustomerService()

@cc.route('/')
def index():
    return "This is an example app"


@cc.route('/api/customers')
def get_all_customers():
    return {
        "users": customer_service.get_all_customers()  # a list of dictionaries
    }
