import pytest
from exception.customer_not_found import CustomerNotFound
from exception.invalid_parameter import InvalidParameter
from controller.customer_controller import customer_service
from model.customer import Customer


def test_get_all_customers(mocker):
    #  Arrange
    def mock_get_all_customers(self):
        returned_records = [(1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500'),
                            (2, 'Jane', 'Doe', '1908-01-01', '1908-01-02', 'a@a.ca', 'M2J 1M5', '555', '555-555-501'),
                            (3, 'test', 'user3', '1908-01-01', '1908-01-03', 'a@a.ca', 'M2J 1M5', '555', '555-555-502')]
        res = []
        for record in returned_records:
            res.append(Customer(record[0], record[1], record[2], record[3], record[4],
                                record[5], record[6], record[7], record[8]))
        return res

    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)
    # Act
    actual = customer_service.get_all_customers()

    # Assert
    assert actual == [{'customer_id': 1,
                       'first_name': 'John',
                       'last_name': 'Doe',
                       'date_of_birth': '1908-01-01',
                       'customer_since': '2000-01-01',
                       'email': 'a@a.ca',
                       'postal_code': 'M2J 1M5',
                       'unit_no': '555',
                       'mobile_phone': '555-555-500'
                       },
                      {'customer_id': 2,
                       'first_name': 'Jane',
                       'last_name': 'Doe',
                       'date_of_birth': '1908-01-01',
                       'customer_since': '1908-01-02',
                       'email': 'a@a.ca',
                       'postal_code': 'M2J 1M5',
                       'unit_no': '555',
                       'mobile_phone': '555-555-501'
                       },
                      {'customer_id': 3,
                       'first_name': 'test',
                       'last_name': 'user3',
                       'date_of_birth': '1908-01-01',
                       'customer_since': '1908-01-03',
                       'email': 'a@a.ca',
                       'postal_code': 'M2J 1M5',
                       'unit_no': '555',
                       'mobile_phone': '555-555-502'
                       }]


def test_get_customer_by_id_1(mocker):
    #  Arrange
    def mock_get_customer_by_id(self, cust_id):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500')
        if cust_id == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    # Act
    actual = customer_service.get_customer_by_id(1)

    # Assert
    assert actual == {'customer_id': 1,
                      'first_name': 'John',
                      'last_name': 'Doe',
                      'date_of_birth': '1908-01-01',
                      'customer_since': '2000-01-01',
                      'email': 'a@a.ca',
                      'postal_code': 'M2J 1M5',
                      'unit_no': '555',
                      'mobile_phone': '555-555-500'
                      }


def test_get_customer_by_id_2(mocker):
    #  Arrange
    def mock_get_customer_by_id(self, cust_id):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500')
        if cust_id == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        customer_service.get_customer_by_id(2)


def test_delete_customer_by_id_1(mocker):
    #  Arrange
    def mock_delete_customer_by_id(self, cust_id):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500')
        if cust_id == 1:
            return returned_record
        else:
            return None

    def mock_get_customer_by_id(self, cust_id):
        return 1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500'

    def mock_get_accounts_by_customer_id(self, cust_id, args):
        return None

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_delete_customer_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_accounts_by_customer_id', mock_get_accounts_by_customer_id)
    # Act
    actual = customer_service.delete_customer_by_id(1)

    # Assert
    assert actual == (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500')


def test_delete_customer_by_id_2(mocker):
    #  Arrange
    def mock_delete_customer_by_id(self, cust_id):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500')
        if cust_id == 1:
            return returned_record
        else:
            return None
    def mock_get_customer_by_id(self, cust_id):
        return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_delete_customer_by_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        customer_service.delete_customer_by_id(2)


def test_add_customer_valid_user(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act
    actual = customer_service.add_customer(Customer(None, 'John', 'Doe', '1908-01-01', None,
                                                    'a@a.ca', 'M2J1M5', '555', '555-555-5000'))
    # Assert
    assert actual == {'customer_id': 1,
                      'first_name': 'John',
                      'last_name': 'Doe',
                      'date_of_birth': '1908-01-01',
                      'customer_since': '2000-01-01',
                      'email': 'a@a.ca',
                      'postal_code': 'M2J 1M5',
                      'unit_no': '555',
                      'mobile_phone': '555-555-5000'
                      }


def test_add_customer_invalid_first_name_1(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, '', 'Doe', '1908-01-01', None,
                                               'a@a.ca', 'M2J 1M5', '555', '555-555-5000'))


def test_add_customer_invalid_first_name_2(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'b', 'Doe', '1908-01-01', None,
                                               'a@a.ca', 'M2J 1M5', '555', '555-555-5000'))


def test_add_customer_invalid_first_name_3(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob marley', 'Doe', '1908-01-01', None,
                                               'a@a.ca', 'M2J 1M5', '555', '555-555-5000'))


def test_add_customer_invalid_first_name_4(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob marley', 'Doe', '1908-01-01', None,
                                               'a@a.ca', 'M2J 1M5', '555', '555-555-5000'))


def test_add_customer_invalid_email(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob', 'Doe', '1908-01-01', None,
                                               'aa.ca', 'M2J 1M5', '555', '555-555-5000'))


def test_add_customer_invalid_postal_code_1(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob', 'Doe', '1908-01-01', None,
                                               'aa.ca', 'M2J-1M5', '555', '555-555-5000'))


def test_add_customer_invalid_postal_code_2(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob', 'Doe', '1908-01-01', None,
                                               'aa.ca', 'M2J61M5', '555', '555-555-5000'))


def test_add_customer_invalid_postal_code_3(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob', 'Doe', '1908-01-01', None,
                                               'aa.ca', '', '555', '555-555-5000'))


def test_add_customer_invalid_mobile_phone_1(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob', 'Doe', '1908-01-01', None,
                                               'aa.ca', '', '555', '555-555-500'))


def test_add_customer_invalid_mobile_phone_2(mocker):
    #  Arrange
    def mock_add_customer(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    # Act and # Assert
    with pytest.raises(InvalidParameter):
        customer_service.add_customer(Customer(None, 'bob', 'Doe', '1908-01-01', None,
                                               'aa.ca', '', '555', ''))


def test_update_customer_valid_user(mocker):
    #  Arrange
    def mock_update_customer_by_id(self, customer):
        returned_record = (1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None
    def mock_get_customer_by_id(self, cust_id):
        return 1, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-500'

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.update_customer_by_id', mock_update_customer_by_id)
    # Act
    actual = customer_service.update_customer_by_id(Customer(None, 'John', 'Doe', '1908-01-01', None,
                                                             'a@a.ca', 'M2J1M5', '555', '555-555-5000'))
    # Assert
    assert actual == {'customer_id': 1,
                      'first_name': 'John',
                      'last_name': 'Doe',
                      'date_of_birth': '1908-01-01',
                      'customer_since': '2000-01-01',
                      'email': 'a@a.ca',
                      'postal_code': 'M2J 1M5',
                      'unit_no': '555',
                      'mobile_phone': '555-555-5000'
                      }


def test_update_customer_invalid_customer_id(mocker):
    #  Arrange
    def mock_update_customer_by_id(self, customer):
        returned_record = (3, 'John', 'Doe', '1908-01-01', '2000-01-01', 'a@a.ca', 'M2J 1M5', '555', '555-555-5000')
        if returned_record[0] == 1:
            return Customer(returned_record[0], returned_record[1], returned_record[2], returned_record[3],
                            returned_record[4], returned_record[5], returned_record[6], returned_record[7],
                            returned_record[8])
        else:
            return None
    def mock_get_customer_by_id(self, cust_id):
        return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.customer_dao.CustomerDao.update_customer_by_id', mock_update_customer_by_id)
    # Act and # Assert
    with pytest.raises(CustomerNotFound):
        customer_service.update_customer_by_id(Customer(3, 'John', 'Doe', '1908-01-01', '2000-01-01',
                                                        'a@a.ca', 'M2J1M5', '555', '555-555-5000'))

