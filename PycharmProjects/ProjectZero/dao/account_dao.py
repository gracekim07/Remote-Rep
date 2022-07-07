import psycopg
from model.account import Account


class AccountDao:

    ## ## GET/customer/accounts

    def get_all_accounts(self):

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts")

                my_list_of_accounts_objs = []

                for account in cur:
                    a_id = account[0]
                    account_balance = account[1]
                    active = account[2]

                    my_account_obj = Account(a_id, account_balance, active)
                    my_list_of_accounts_objs.append(my_account_obj)

                return my_list_of_accounts_objs

        ## GET/customer/1/accounts

    @staticmethod
    def get_all_accounts_by_customer_id(customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s", (customer_id,))

                all_accounts_details = cur.fetchall()
                print(all_accounts_details)
                return {"account_details": all_accounts_details}

    @staticmethod
    def get_account_by_id(customer_id, account_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s and id = %s", (customer_id, account_id))

                account_list = cur.fetchall()
                print(type(account_list[0]))
                return {"account details received": account_list[0]}

    # def get_all_accounts_by_account_id(self, account_id):
    #     with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
    #                          password="Iloveyou27") as conn:
    #
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM accounts WHERE account_id = %s", (account_id,))
    #
    #
    #                 accounts_list = []
    #
    #                 for row in cur:
    #                     account_list.append(Account(row[0], row[1], row[2]))
    #
    #                 return account_list

    def add_account(self, account_object):
        account_balance_to_add = account_object.account_balance
        customer_id_to_add = account_object.customer_id

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (account_balance, customer_id) VALUES (%s, %s) RETURNING *",
                            (account_balance_to_add,
                             customer_id_to_add))

                account_row_that_was_just_inserted = cur.fetchone()
                conn.commit()
                return Account(account_row_that_was_just_inserted[0], account_row_that_was_just_inserted[1],
                               account_row_that_was_just_inserted[2], account_row_that_was_just_inserted[3])
