import pytest

from controller.account_controller import account_service
from exception.customer_not_found import CustomerNotFound
from exception.account_not_found import AccountNotFound
from exception.unauthorized_access import UnauthorizedAccess
from exception.invalid_parameter import InvalidParameter
from controller.customer_controller import customer_service
from model import account
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
        return True

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.add_account_by_customer_id', mock_add_account_by_customer_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.add_account_by_customer_id(2, acc)


def test_get_accounts_by_customer_id_invalid_user(mocker):
    #  Arrange

    def mock_get_accounts_by_customer_id(self, cust_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1:
            return returned_record
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_accounts_by_customer_id', mock_get_accounts_by_customer_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.add_account_by_customer_id(10, [{"amountGreaterThan": 200}, {"amountLessThan": 1000}])


def test_get_accounts_by_customer_id_valid_user_two_valid_params(mocker):
    #  Arrange

    def mock_get_accounts_by_customer_id_agt_alt(self, cust_id, agt, alt):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1:
            return [Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])]
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):

        return True

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_accounts_by_customer_id_agt_alt',
                 mock_get_accounts_by_customer_id_agt_alt)
    # Act
    actual = account_service.get_accounts_by_customer_id(1, {"amountGreaterThan": 200, "amountLessThan": 1000})

    # Assert
    assert actual == [{
        "account_id": actual[0]['account_id'],
        "type_id": actual[0]['type_id'],
        "currency_id": actual[0]['currency_id'],
        "balance": actual[0]['balance']

    }]

def test_get_accounts_by_customer_id_valid_user_agt_valid_param(mocker):
    #  Arrange

    def mock_get_accounts_by_customer_id_agt(self, cust_id, agt):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1:
            return Account(returned_record[0], returned_record[1], returned_record[2], returned_record[3])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_accounts_by_customer_id_agt', mock_get_accounts_by_customer_id_agt)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.add_account_by_customer_id(1, [{"amountGreaterThan": 200}])


def test_get_accounts_by_customer_id_valid_user_alt_valid_param(mocker):
    #  Arrange

    def mock_get_accounts_by_customer_id_alt(self, cust_id, alt):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1:
            return Account(returned_record[0], returned_record[1], returned_record[2], returned_record[3])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_accounts_by_customer_id_alt', mock_get_accounts_by_customer_id_alt)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.add_account_by_customer_id(1, [{"amountLessThan": 1000}])


def test_get_customer_account_by_customer_id_valid_user_valid_account(mocker):
    #  Arrange

    def mock_get_customer_account_by_account_id(self, cust_id, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1 and account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id',
                 mock_get_customer_account_by_account_id)
    # Act
    actual = account_service.get_customer_account_by_account_id(1, 3)

    # Assert
    assert actual == {
        "account_id": actual['account_id'],
        "type_id": actual['type_id'],
        "currency_id": actual['currency_id'],
        "balance": actual['balance']

    }


def test_get_customer_account_by_customer_id_invalid_user_valid_account(mocker):
    #  Arrange

    def mock_get_customer_account_by_account_id(self, cust_id, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1 and account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id',
                 mock_get_customer_account_by_account_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.get_customer_account_by_account_id(12, 2)


def test_get_customer_account_by_customer_id_invalid_user_valid_account_2(mocker):
    #  Arrange

    def mock_get_customer_account_by_account_id(self, cust_id, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1 and account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id',
                 mock_get_customer_account_by_account_id)
    # Act and  # Assert
    with pytest.raises(UnauthorizedAccess):
        account_service.get_customer_account_by_account_id(1, 2)


def test_get_customer_account_by_customer_id_valid_user_invalid_account(mocker):
    #  Arrange

    def mock_get_customer_account_by_account_id(self, cust_id, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if cust_id == 1 and account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id',
                 mock_get_customer_account_by_account_id)
    # Act and  # Assert
    with pytest.raises(AccountNotFound):
        account_service.get_customer_account_by_account_id(1, 11)


def test_update_customer_account_by_account_id_valid_user_valid_account(mocker):
    # Arrange
    def mock_update_account_by_id(self, acc):

        return acc


    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, cust_id):
        if cust_id != 3:
            return None
        return True

    def mock_get_customer_account_by_account_id(self, cust_id,account_id):

        return True

    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id', mock_get_customer_account_by_account_id)
    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.update_account_by_id',
                 mock_update_account_by_id)

    # Act
    actual = account_service.update_customer_account_by_account_id(1, Account(3, 1, 1, 5000))

    # Assert
    assert actual == {
        "account_id": actual['account_id'],
        "type_id": actual['type_id'],
        "currency_id": actual['currency_id'],
        "balance": actual['balance']

    }


def test_delete_customer_account_by_account_id_valid_user_valid_account_association_false(mocker):
    # Arrange

    def mock_delete_account_by_id(self, acc_id):

        return True

    def mock_get_customer_by_id(self, cust_id):

        return True

    def mock_get_account_by_id(self, cust_id):

        return True

    def mock_get_customer_account_by_account_id(self, cust_id,account_id):

        return True
    def mock_check_for_joined_accounts_by_id(self, account_id):
        return False

    mocker.patch('dao.account_dao.AccountDao.check_for_joined_accounts_by_id', mock_check_for_joined_accounts_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id', mock_get_customer_account_by_account_id)
    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.delete_account_by_id',
                 mock_delete_account_by_id)

    # Act
    actual = account_service.delete_customer_account_by_account_id(1, 3)

    # Assert
    assert actual == {"message": f"Customer account with ID: 3 and its associations were successfully deleted!"}


def test_delete_customer_account_by_customer_id_invalid_user_valid_account(mocker):
    #  Arrange

    def mock_delete_account_by_id(self, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.delete_account_by_id',
                 mock_delete_account_by_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        account_service.delete_customer_account_by_account_id(2, 3)

def test_delete_customer_account_by_customer_id_valid_user_invalid_account(mocker):
    #  Arrange

    def mock_delete_account_by_id(self, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    def mock_get_customer_account_by_account_id(self, cust_id, account_id):
        return None

    def mock_check_for_joined_accounts_by_id(self, cust_id, account_id):
        return None

    mocker.patch('dao.account_dao.AccountDao.check_for_joined_accounts_by_id', mock_check_for_joined_accounts_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id', mock_get_customer_account_by_account_id)
    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.delete_account_by_id',
                 mock_delete_account_by_id)
    # Act and  # Assert
    with pytest.raises(UnauthorizedAccess):
        account_service.delete_customer_account_by_account_id(1, 2)


def test_delete_customer_account_by_customer_id_valid_user_invalid_account(mocker):
    #  Arrange

    def mock_delete_account_by_id(self, account_id):
        returned_record = {
            "account_id": 1,
            "balance": 100,
            "currency_id": 1,
            "type_id": 1
        }
        if account_id == 3:
            return Account(returned_record["account_id"], returned_record["type_id"], returned_record["currency_id"],
                           returned_record["balance"])
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        if cust_id != 1:
            return None
        return True

    def mock_get_account_by_id(self, account_id):
        if account_id == 2 or account_id == 3:
            return True
        return None

    def mock_get_customer_account_by_account_id(self, cust_id, account_id):
        return True

    def mock_check_for_joined_accounts_by_id(self, account_id):
        return None

    mocker.patch('dao.account_dao.AccountDao.check_for_joined_accounts_by_id', mock_check_for_joined_accounts_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id',
                 mock_get_customer_account_by_account_id)
    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.delete_account_by_id',
                 mock_delete_account_by_id)
    # Act
    #
    #


    actual = account_service.delete_customer_account_by_account_id(1, 2)
    # Assert
    assert actual == {"message": f"Customer account with ID: 2 is not associated with any customers"}



def test_delete_customer_account_by_account_id_valid_user_valid_account_association_true(mocker):
    # Arrange

    def mock_delete_account_by_id(self, acc_id):

        return True

    def mock_get_customer_by_id(self, cust_id):

        return True

    def mock_get_account_by_id(self, cust_id):

        return True

    def mock_get_customer_account_by_account_id(self, cust_id,account_id):

        return True
    def mock_delete_joined_association(self, account_id,cust_id):
        return 1,3

    def mock_check_for_joined_accounts_by_id(self, account_id):
        return True

    mocker.patch('dao.account_dao.AccountDao.delete_joined_association', mock_delete_joined_association)

    mocker.patch('dao.account_dao.AccountDao.check_for_joined_accounts_by_id', mock_check_for_joined_accounts_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_customer_account_by_account_id', mock_get_customer_account_by_account_id)
    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.delete_account_by_id',
                 mock_delete_account_by_id)

    # Act
    actual = account_service.delete_customer_account_by_account_id(1, 3)

    # Assert
    assert actual == {"message": f"Customer account with ID: 1 cannot be deleted because customer "
                                   f"with ID: 3 is not the only account owner, however this "
                                   f"customer is no longer associated with this account"}