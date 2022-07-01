class AccountType:
    def __init__(self,
                 account_type_id,
                 account_type_name):
        self.__account_type_id = account_type_id
        self.__account_type_name = account_type_name

    def get_account_type_id(self):
        return self.__account_type_id

    def get_account_type_name(self):
        return self.__account_type_name

    def set_account_type_id(self, value):
        self.__account_type_id = value

    def set_account_type_name(self, value):
        self.__account_type_name = value

    def to_dict(self):
        return {
            'account_type_id': self.get_account_type_id(),
            'account_type_name': self.get_account_type_name()
        }
