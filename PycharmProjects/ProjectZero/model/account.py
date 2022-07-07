class Account:
    def __init__(self, t_id, account_balance, customer_id):
        self.id = t_id
        self.account_balance = account_balance
        self.customer_id = customer_id

    def to_dict(self):
        return {
            "id": self.id,
            "account_balance": self.account_balance,
            "customer_id": self.customer_id
        }
