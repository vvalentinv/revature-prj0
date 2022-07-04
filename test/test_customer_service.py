import pytest
from exception.customer_not_found import CustomerNotFound
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
    print(actual)
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
    print(actual)
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

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_delete_customer_by_id)
    # Act
    actual = customer_service.delete_customer_by_id(1)
    print(actual)
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

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_delete_customer_by_id)
    # Act and  # Assert
    with pytest.raises(CustomerNotFound):
        customer_service.delete_customer_by_id(2)

