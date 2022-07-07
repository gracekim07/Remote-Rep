from flask import Blueprint
from flask import request
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError
from service.account_service import AccountService
from model.account import Account

tc = Blueprint('account_controller', __name__)


account_service = AccountService()

@tc.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404



## Get accounts in range
@tc.route('/customers/<customer_id>/accounts/range')
def get_customer_accounts(customer_id):
    dgt = request.args.get('amountGreaterThan')
    dlt = request.args.get('amountLessThan')
    try:
        return account_service.get_customer_accounts(customer_id, dgt, dlt), 201
    except InvalidParameterError as e:
        return {

        "message": f"{e}"
    }, 400





@tc.route('/customers/<customer_id>/accounts', methods=['POST'])
def add_account():
    account_json_dictionary = request.get_json()
    account_object = Account(None, account_json_dictionary['account_balance'], account_json_dictionary['customer_id'], None)
    try:
        return account_service.add_customer(account_object), 201  # Dictionary representation of the newly added user
        # 201 created
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400





@tc.route('/customers/<customer_id>/accounts/<account_id>')
def get_account_by_id(customer_id, account_id):
    return AccountService.get_account_by_id(customer_id, account_id)



#     try:
#         return {
#         "accounts": account_service.get_all_accounts_by_customer_id(customer_id, account_id)
#         }
#     except CustomerNotFoundError as e:
#         return {
#                "message": str(e)
#            }, 404

#     try:
#         return {
#             "accounts": account_service.get_all_accounts_by_customer_id_account_id(customer_id, account_id)
#         }
#     except CustomerNotFoundError as e:
#         return {
#                    "message": str(e)
#                }, 404
















@tc.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def edit_account_by_customer_id_and_account_id(customer_id, account_id):
    pass





@tc.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_customer_id_and_account_id(customer_id, account_id):
    pass

