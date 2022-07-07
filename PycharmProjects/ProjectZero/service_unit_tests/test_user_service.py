import dao.customer_dao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_already_exists import CustomerAlreadyExistsError
from exception.customer_not_found import CustomerNotFoundError
from model.customer import Customer
from service.customer_service import CustomerService
import pytest


def test_get_all_customers(mocker):

    def mock_get_all_customers(self):
        return [Customer(1, 'test', '00-00-0001', True), Customer(2, 'testing', '00-00-0002', False)]

    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)

    customer_service = CustomerService()


    actual = customer_service.get_all_customers()


    assert actual == [
        {
            "id": 1,
            "firstname": "test",
            "birthday": "00-00-0001",
            "active": True
        },
        {
            "id": 2,
            "firstname": "testing",
            "birthday": "000-000-0002",
            "active": False
        }
    ]


def test_get_customer_by_id_positive(mocker):


    def mock_get_customer_by_id(self, customer_id):
        if customer_id == "1":
            return Customer(1, 'test', '000-000-0001', True)
        else:
            return None


    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)

    customer_service = CustomerService()


    actual = customer_service.get_customer_by_id("1")


    assert actual == {
        "id": 1,
        "firstname": "test",
        "birthday": "00-00-0001",
        "active": True
    }



def test_get_customer_by_id_negative(mocker):

    def mock_get_customer_by_id(self, customer_id):
        if customer_id == "1":
            return Customer(1, 'test', '000-000-0001', True)
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)

    customer_service = CustomerService()



    # Method 1 of testing for exceptions occurring
    # try:
    #     actual = user_service.get_user_by_id("1000")
    #
    #     assert False  # Fail the test if we make it to this line of code. We should never reach this line if an exception
    #     # is actually raised
    # except UserNotFoundError as e:
    #     assert True

    # Method 2
    with pytest.raises(CustomerNotFoundError) as excinfo:
        actual = customer_service.get_customer_by_id("1000")

    # Testing for an exception message
    assert str(excinfo.value) == "Customer with id 1000 was not found"


def test_delete_customer_by_id_positive(mocker):

    def mock_delete_customer_by_id(self, customer_id):
        if customer_id == "1":
            return True
        else:
            return False

    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)

    customer_service = CustomerService()


    actual = customer_service.delete_customer_by_id("1")


    assert actual is None


def test_delete_customer_by_id_negative(mocker):

    def mock_delete_customer_by_id(self, customer_id):
        if customer_id == "1":
            return True
        else:
            return False

    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)

    customer_service = CustomerService()


    with pytest.raises(CustomerNotFoundError) as excinfo:
        customer_service.delete_customer_by_id("205")


    assert str(excinfo.value) == "Customer with id 205 was not found"

def test_add_customer_positive(mocker):

    def mock_get_customer_by_firstname(self, firstname):
        if firstname == "Testy":
            return None

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_firstname", mock_get_customer_by_firstname)

    customer_obj_to_add = Customer(None, "testy", "12-26-2001", None)

    def mock_add_customer(self, customer_obj):
        if customer_obj == customer_obj_to_add:
            return Customer(1, "Testy", "12-26-2001", True)
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.add_customer", mock_add_customer)

    customer_service = CustomerService()



    actual = customer_service.add_customer(customer_obj_to_add)


    assert actual == {
        "id": 1,
        "firstname": "testy",
        "birthday": "12-26-2001",
        "active": True
    }


def test_add_customer_negative_spaces_in_firstname(mocker):

    customer_obj_to_add = Customer(None, "   bachy   21  ", "512-826-0001", None)

    customer_service = CustomerService()



    with pytest.raises(InvalidParameterError) as excinfo:
        actual = customer_service.add_customer(customer_obj_to_add)

    assert str(excinfo.value) == "Firstname cannot contain spaces"

def test_add_customer_negative_length_is_less_than_6_for_firstname(mocker):

    customer_obj_to_add = Customer(None, "bach1", "512-826-0001", None)

    customer_service = CustomerService()



    with pytest.raises(InvalidParameterError) as excinfo:
        actual = customer_service.add_customer(customer_obj_to_add)

    assert str(excinfo.value) == "Firstname must be at least 6 characters"

def test_add_customer_negative_firstname_already_exists(mocker):

    customer_object_to_add = Customer(None, "bachy21", "512-826-0001", None)

    def mock_get_customer_by_firstname(self, firstname):
        if firstname == "bachy21":
            return Customer(1, "bachy21", "512-826-0001", True)

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_firstname", mock_get_customer_by_firstname)

    customer_service = CustomerService()


    with pytest.raises(CustomerAlreadyExistsError) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)

    assert str(excinfo.value) == "Customer with firstname bachy21 already exists"

def test_update_customer_by_id_positive(mocker):

    update_customer_obj = Customer(10, "john_doe", "12-26-1111", True)

    def mock_update_customer_by_id(self, customer_obj):
        if customer_obj.id == 10:
            return Customer(10, "john_doe", "12-26-2011", True)
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.update_customer_by_id", mock_update_customer_by_id)

    customer_service = CustomerService()


    actual = customer_service.update_customer_by_id(update_customer_obj)


    assert actual == {
        "id": 10,
        "firstname": "john_doe",
        "birthday": "12-26-2011",
        "active": True
    }

def test_update_customer_by_id_positive(mocker):

    update_customer_obj = Customer(100, "john_doe", "12-26-2011", True)

    def mock_update_customer_by_id(self, customer_obj):
        if customer_obj.id == 10:
            return Customer(10, "john_doe", "12-26-2011", True)
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.update_customer_by_id", mock_update_customer_by_id)

    customer_service = CustomerService()


    with pytest.raises(CustomerNotFoundError) as excinfo:
        actual = customer_service.update_customer_by_id(update_customer_obj)

    assert str(excinfo.value) == "Customer with id 100 was not found"