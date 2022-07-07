import pytest

from controller.account_controller import account_service
from exception.customer_not_found import CustomerNotFound
from exception.invalid_parameter import InvalidParameter
from controller.customer_controller import customer_service
from model.account import Account
from model.customer import Customer


def test_add_account_by_customer_id_1(mocker):
    #  Arrange

    def mock_add_account_by_customer_id(self, account, cust_id):

        if cust_id == 1:
            return Account(1, 1, 1, 5000)
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.add_account_by_customer_id', mock_add_account_by_customer_id)
    # Act
    actual = account_service.add_account_by_customer_id(Account(1, 1, 1, 5000), 1)
    # Assert
    assert actual == {
        "account_id": actual['account_id'],
        "type_id": actual['type_id'],
        "currency_id": actual['currency_id'],
        "balance": actual['balance']

    }


def test_add_account_by_customer_id_2(mocker):
    #  Arrange
    acc = Account(None, 1, 1, 5000)

    def mock_add_account_by_customer_id(self, cust_id, account):
        returned_record = (1, 1, 1, 5000)
        if cust_id == 1:
            return returned_record
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.add_account_by_customer_id', mock_add_account_by_customer_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.add_account_by_customer_id(2, acc)
