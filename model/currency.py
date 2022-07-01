class Currency:
    def __init__(self,
                 currency_id,
                 currency_name):
        self.__currency_id = currency_id
        self.__currency_name = currency_name

    def get_currency_id(self):
        return self.__currency_id

    def get_currency_name(self):
        return self.__currency_name

    def set_currency_id(self, value):
        self.__currency_id = value

    def set_currency_name(self, value):
        self.__currency_name = value

    def to_dict(self):
        return {
            'currency_id': self.get_currency_id(),
            'currency_name': self.get_currency_name()
        }
