from flask import Blueprint, request
from model.account import Account
from service.account_service import AccountService
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError

ac = Blueprint('account_controller', __name__)
account_service = AccountService()


@ac.route('/api/customers/{customer_id}/accounts', methods=['POST'])
def add_account_by_customer_id(customer_id):
    acc = request.get_json()
    print(acc)
    account = Account(None, acc['type_id'], acc['currency_id'], acc['balance'])

    try:
        return account_service.add_account_by_customer_id(account, customer_id), 201  # Dictionary representation of the newly added user
        # 201 created
    except InvalidParameterError as e:
        return {
                   "message": str(e)
               }, 400
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404

