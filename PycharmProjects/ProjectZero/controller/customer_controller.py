from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError

uc = Blueprint('customer_controller', __name__)
customer_service = CustomerService()




@uc.route('/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }





@uc.route('/customers/<customer_id>')
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404




@uc.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer_by_id(customer_id):
    try:
        customer_service.delete_customer_by_id(customer_id)

        return {
            "message": f"Customer with id {customer_id} deleted successfully"
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
#
#
#
#
@uc.route('/customers/<customer_id>', methods=['PUT'])
def update_customer_by_id(customer_id):
    try:
        json_dictionary = request.get_json()
        return customer_service.update_customer_by_id(Customer(customer_id, json_dictionary['firstname'], json_dictionary['birthday'], json_dictionary['active']))
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
#
#
#
#
#
@uc.route('/customers', methods=['POST'])
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['firstname'], customer_json_dictionary['birthday'], None)
    try:
        return customer_service.add_customer(customer_object), 201  # Dictionary representation of the newly added user
        # 201 created
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400