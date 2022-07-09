import re
from utility.db_connection import pool
from exception.invalid_parameter import InvalidParameter


def check_date(date):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_date - interval '16 year' <= %s;", (date,))
            if cur.fetchone()[0]:
                raise InvalidParameter("Minimum Customer age must be 16 years-old")
            return True


def validate_name(string):
    reg_invalid_character = r"[^a-zA-Z]"

    if not string:
        raise InvalidParameter("Names cannot be blank")
    if re.findall(reg_invalid_character, string):
        raise InvalidParameter("Names must have only letters a-zA-Z and no other characters or spaces")
    elif len(string) > 30:
        raise InvalidParameter("Names are limited to 30 letters ")
    elif len(string) < 2:
        raise InvalidParameter("Names must have at least 2 letters")
    else:
        return True


def validate_email(string):
    reg_email = r"[^@]+@[^@]+\.[^@]+"
    if not string:
        raise InvalidParameter("email cannot be blank")
    if not re.match(reg_email, string):
        raise InvalidParameter("accepted email address format is <username>@<company>.<domain>")
    return True


def validate_postal_code(string):
    reg_invalid_character = r"[^a-zA-Z0-9]"
    if not string:
        raise InvalidParameter("Postal code cannot be blank")
    if re.findall(reg_invalid_character, string):
        raise InvalidParameter("Postal code must have only letters a-zA-Z and/or 0-9 numbers")
    elif not 4 < len(string.replace(" ", "")) < 7:
        raise InvalidParameter("Postal code length must be equal to 5 or 6 without any space")
    return True


def validate_phone(string):
    reg_phone = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
    if not string:
        raise InvalidParameter("mobile phone cannot be blank")
    if not re.match(reg_phone, string):
        raise InvalidParameter("mobile phone format <555-555-5555>")
    return True


def validate_args(args):
    if args:
        agt = args.get("amountGreaterThan")
        alt = args.get("amountLessThan")
        len_args = len(args)
    else:
        return None
    if not agt and 'amountLessThan' in args.keys() and len_args == 2:
        raise InvalidParameter('the expected parameter name is "amountGreaterThan" with positive Integer values')
    elif not alt and 'amountGreaterThan' in args.keys() and len_args == 2:
        raise InvalidParameter('the expected parameter name is "amountLessThan" with positive Integer values')

    if agt:
        try:
            agt = int(agt)
        except ValueError as e:
            raise InvalidParameter('"amountGreaterThan" and "amountLessThan" '
                                   'represent cents values(enter integer values)')
    if alt:
        try:
            alt = int(alt)
        except ValueError as e:
            raise InvalidParameter('"amountGreaterThan" and "amountLessThan" '
                                   'represent cents values(enter integer values)')

    if agt and alt and (agt < 0 or alt < 0):
        raise InvalidParameter('"amountGreaterThan" and "amountLessThan" must be positive values')
    elif agt and alt and agt > alt:
        raise InvalidParameter('"amountGreaterThan" is expected to be equal or smaller than "amountLessThan" '
                               'and positive')
    return True


def validate_balance(balance):
    if balance < 0:
        raise InvalidParameter("Update balance with positive values only")
    return balance
