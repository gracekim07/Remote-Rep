from dao.customer_dao import CustomerDao
from dao.account_dao import AccountDao
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError


class AccountService:

    def __init__(self):

        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts(self):
        list_of_accounts = self.customer_dao.get_all_accounts()
        list_of_accounts_formatted = []
        for a in list_of_accounts:
            id = a[0]
            account_id = a[1]
            account_balance = a[2]
            active = a[3]

            my_account_obj = (id, account_id, account_balance, active)
            list_of_accounts_formatted.append(my_account_obj)

    @staticmethod
    def get_account_by_id(customer_id, account_id):
        details_received = AccountDao.get_account_by_id(customer_id, account_id)
        details_tuple = details_received["account details received"]
        return {f"Details of account {account_id} of customer having id {customer_id}": {
            "account num": details_tuple[0],
            "balance": details_tuple[1],
            "customer_id": details_tuple[2]
        }}

        # if self.customer_dao.get_customer_by_id(customer_id) is None:
        #     raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")
        #
        # return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))

    ##Add account (not working)

    def add_account(self, account_object):

        added_account_object = self.customer_dao.add_account(account_object)
        return added_account_object.to_dict()

    # Get account in a range        NOT WORKING

    def get_customer_accounts(self, customer_id, dgt, dlt):
        customer_obj = self.customer_dao.get_all_customers(customer_id)
        accounts = customer_obj.get_all_accounts()
        acct_list = {}
        for account in accounts:
            amount = self.account_dao.get_all_accounts(account, customer_id).get_dollars()
            if dgt != None and dlt != None:
                if amount >= int(dgt) and amount < int(dlt):
                    acct_list.update({account: self.account_dao.get_all_accounts(account, customer_id).to_dict()})
            elif dgt == None and dlt != None:
                if amount < int(dlt):
                    acct_list.update({account: self.account_dao.get_all_accounts(account, customer_id).to_dict()})
            elif dgt != None and dlt == None:
                if amount >= int(dgt):
                    acct_list.update({account: self.account_dao.get_all_accounts(account, customer_id).to_dict()})

            return acct_list

    # def get_customer_accounts(self, dgt, dlt):
    #     customer_obj = self.customer_dao.get_all_customers()
    #     accounts = customer_obj.get_all_accounts()
    #     acct_list = {}
    #     for account in accounts:
    #         amount = self.account_dao.get_all_accounts().get_dollars()
    #         if dgt != None and dlt != None:
    #             if amount >= int(dgt) and amount < int(dlt):
    #                 acct_list.update({account: self.account_dao.get_all_accounts().to_dict()})
    #         elif dgt == None and dlt != None:
    #             if amount < int(dlt):
    #                 acct_list.update({account: self.account_dao.get_all_accounts().to_dict()})
    #         elif dgt != None and dlt == None:
    #             if amount >= int(dgt):
    #                 acct_list.update({account: self.account_dao.get_all_accounts().to_dict()})
    #
    #     return acct_list

    #
    # def get_account_by_id(self, customer_id, account_id):
    #     return self.account_dao.get_all_accounts(account_id, customer_id).to_dict()
