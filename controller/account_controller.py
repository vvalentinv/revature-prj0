from flask import Blueprint, request
from model.account import Account
from service.account_service import AccountService
from exception.customer_not_found import CustomerNotFound
from exception.invalid_parameter import InvalidParameter
from exception.account_not_found import AccountNotFound
from exception.unauthorized_access import UnauthorizedAccess

ac = Blueprint('account_controller', __name__)
account_service = AccountService()


@ac.route('/api/customers/<customer_id>/accounts', methods=['POST'])
def add_account_by_customer_id(customer_id):
    acc = request.get_json()
    account = Account(None, acc['type_id'], acc['currency_id'], acc['balance_in_cents'])

    try:
        # Dictionary representation of the newly added user
        return account_service.add_account_by_customer_id(account, customer_id), 201
        # 201 created
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400
    except CustomerNotFound as e:
        return {
                   "message": str(e)
               }, 404


@ac.route('/api/customers/<customer_id>/accounts')
def get_accounts_by_customer_id(customer_id):
    args = request.args
    try:
        return {"accounts": account_service.get_accounts_by_customer_id(customer_id, args)}, 200
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400
    except CustomerNotFound as e:
        return {
                   "message": str(e)
               }, 404


@ac.route('/api/customers/<customer_id>/accounts/<account_id>')
def get_customer_account_by_account_id(customer_id, account_id):
    try:
        return account_service.get_customer_account_by_account_id(customer_id, account_id), 200
    except UnauthorizedAccess as e:
        return {
                   "message": str(e)
               }, 403
    except CustomerNotFound as e:
        return {
                   "message": str(e)
               }, 404
    except AccountNotFound as e:
        return {
                   "message": str(e)
               }, 404


@ac.route('/api/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def update_customer_account_by_account_id(customer_id, account_id):
    acc = request.get_json()
    try:
        return account_service.update_customer_account_by_account_id(customer_id,
                                                                     Account(account_id, acc.get('type_id'),
                                                                             acc.get('currency_id'),
                                                                             acc.get('balance_in_cents'))), 200
    except UnauthorizedAccess as e:
        return {
                   "message": str(e)
               }, 403
    except CustomerNotFound as e:
        return {
                   "message": str(e)
               }, 404
    except AccountNotFound as e:
        return {
                   "message": str(e)
               }, 404
    except InvalidParameter as e:
        return {
                   "message": str(e)
               }, 400


@ac.route('/api/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_customer_account_by_account_id(customer_id, account_id):
    try:
        return account_service.delete_customer_account_by_account_id(customer_id, account_id), 200
    except UnauthorizedAccess as e:
        return {
                   "message": str(e)
               }, 403
    except CustomerNotFound as e:
        return {
                   "message": str(e)
               }, 404
    except AccountNotFound as e:
        return {
                   "message": str(e)
               }, 404
