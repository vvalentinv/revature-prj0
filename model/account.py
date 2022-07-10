class Account:
    def __init__(self,
                 account_id,
                 type_id,
                 currency_id,
                 balance_in_cents):
        self.__account_id = account_id
        self.__type_id = type_id
        self.__currency_id = currency_id
        self.__balance_in_cents = balance_in_cents

    def get_account_id(self):
        return self.__account_id

    def get_type_id(self):
        return self.__type_id

    def get_currency_id(self):
        return self.__currency_id

    def get_balance_in_cents(self):
        return self.__balance_in_cents

    def set_type_id(self, value):
        self.__type_id = value

    def set_account_id(self, value):
        self.__account_id = value

    def set_currency_id(self, value):
        self.__currency_id = value

    def set_balance_in_cents(self, value):
        self.__balance_in_cents = value

    def to_dict(self):
        return {
            'account_id': self.get_account_id(),
            'type_id': self.get_type_id(),
            'currency_id': self.get_currency_id(),
            'balance_in_cents': self.get_balance_in_cents()
        }
