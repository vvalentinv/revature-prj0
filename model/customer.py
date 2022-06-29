class Customer:
    def __init__(self,
                 customer_id,
                 first_name,
                 last_name,
                 date_of_birth,
                 customer_since,
                 email,
                 postal_code,
                 unit_no,
                 mobile_phone):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__customer_since = customer_since
        self.__email = email
        self.__postal_code = postal_code
        self.__unit_no = unit_no
        self.__mobile_phone = mobile_phone

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_customer_since(self):
        return self.__customer_since

    def get_email(self):
        return self.__email

    def get_postal_code(self):
        return self.__postal_code

    def get_unit_no(self):
        return self.__unit_no

    def get_mobile_phone(self):
        return self.__mobile_phone

    def set_first_name(self, value):
        self.__first_name = value

    def set_customer_id(self, value):
        self.__customer_id = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_date_of_birth(self, value):
        self.__date_of_birth = value

    def set_customer_since(self, value):
        self.__customer_since = value

    def set_email(self, value):
        self.__email = value

    def set_postal_code(self, value):
        self.__postal_code = value

    def set_unit_no(self, value):
        self.__unit_no = value

    def set_mobile_phone(self, value):
        self.__mobile_phone = value

    def to_dict(self):
        return {
            'customer_id': self.get_customer_id(),
            'first_name': self.get_first_name(),
            'last_name': self.get_last_name(),
            'date_of_birth': self.get_date_of_birth(),
            'customer_since': self.get_customer_since(),
            'email': self.get_email(),
            'postal_code': self.get_postal_code(),
            'unit_no': self.get_unit_no(),
            'mobile_phone': self.get_mobile_phone()
        }
