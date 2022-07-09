from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.customer_not_found import CustomerNotFound
from exception.invalid_parameter import InvalidParameter

cc = Blueprint('customer_controller', __name__)
customer_service = CustomerService()


@cc.route('/')
def index():
    desc = "<p>How to use this API</p>" \
        "<p>'POST '/customers`: Creates a new customer</p>" \
        "<p>`GET /customers`: Gets all customers</p>" \
        "<p>`GET /customers/{customer_id}`: Get customer with an id of X (if the customer exists)</p>" \
        "<p>`PUT /customers/{customer_id}`: Update customer with an id of X (if the customer exists)</p>" \
        "<p>`DELETE /customers/{customer_id}`: Delete customer with an id of X (if the customer exists)</p>" \
        "<p>`POST /customers/{customer_id}/accounts`: Create a new account for a customer with id of X (if customer " \
        "exists)</p>" \
        "<p>'GET /customers/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300`: Get all accounts" \
        " for customer having id of X with balances between Y and Z (if customer exists)</p>" \
        "<p>`GET /customers/{customer_id}/accounts/{account_id}`: Get account with id of Y belonging to the customer " \
        "having id of X (if customer and account exist AND if account belongs to customer)</p>" \
        "<p>`PUT /customers/{customer_id}/accounts/{account_id}`: Update account with id of Y belonging to customer" \
        " having id of X (if customer and account exist AND if account belongs to customer)</p>" \
        "<p>`DELETE /customers/{customer_id}/accounts/{account_id}`: Delete account with id of Y belonging to the " \
        "customer having id of X (if customer and account exist AND if account belongs to customer)</p>"

    return desc


@cc.route('/api/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()  # a list of dictionaries
    }, 200


@cc.route('/api/customers/<customer_id>')  # GET /api/customers/<customer_id>
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)  # dictionary
    except CustomerNotFound as e:
        return {
                   "message": str(e)
               }, 404


@cc.route('/api/customers', methods=['POST'])  
def add_customer():
    cust = request.get_json()
    customer = Customer(None, cust['first_name'], cust['last_name'],
                        cust['date_of_birth'], None, cust['email'],
                        cust['postal_code'], cust['unit_no'],
                        cust['mobile_phone'])
    try:
        return customer_service.add_customer(customer), 201  # Dictionary representation of the newly added user
        # 201 created
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400


@cc.route('/api/customers/<customer_id>', methods=['PUT'])
def update_customer_by_id(customer_id):
    cust_attr_to_update = request.get_json()
    try:
        return customer_service.update_customer_by_id(Customer(
            customer_id, cust_attr_to_update['first_name'], cust_attr_to_update['last_name'], None, None,
            cust_attr_to_update['email'], cust_attr_to_update['postal_code'],
            cust_attr_to_update['unit_no'], cust_attr_to_update['mobile_phone']))
    except CustomerNotFound as e:
        return {"message": str(e)}, 404
    except InvalidParameter as e:
        return {"message": str(e)}, 400


@cc.route('/api/customers/<customer_id>', methods=['DELETE'])
def delete_customer_by_id(customer_id):
    try:
        deleted_cust = customer_service.delete_customer_by_id(customer_id)
    except CustomerNotFound as e:
        return {"message": str(e)}, 404
    if delete_customer_by_id:
        return {"message": f"The customer with account_id: {deleted_cust[0]} was deleted"}
