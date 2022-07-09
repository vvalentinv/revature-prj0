class Account:
    def __init__(self,
                 account_id,
                 type_id,
                 currency_id,
                 balance):
        self.__account_id = account_id
        self.__type_id = type_id
        self.__currency_id = currency_id
        self.__balance = balance

    def get_account_id(self):
        return self.__account_id

    def get_type_id(self):
        return self.__type_id

    def get_currency_id(self):
        return self.__currency_id

    def get_balance(self):
        return self.__balance

    def set_type_id(self, value):
        self.__type_id = value

    def set_account_id(self, value):
        self.__account_id = value

    def set_currency_id(self, value):
        self.__currency_id = value

    def set_balance(self, value):
        self.__balance = value

    def to_dict(self):
        return {
            'account_id': self.get_account_id(),
            'type_id': self.get_type_id(),
            'currency_id': self.get_currency_id(),
            'balance': self.get_balance()
        }
