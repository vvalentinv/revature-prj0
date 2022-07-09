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
    args_length = 0
    if args:
        args_length = len(args)
    if args_length == 2:
        if 'amountLessThan' in args.keys():
            pass
        else:
            raise InvalidParameter('the expected parameter name is "amountLessThan" ')
        if 'amountGreaterThan' in args.keys():
            pass
        else:
            raise InvalidParameter('the expected parameter name is "amountGreaterThan" ')
        if 0 <= float(args['amountGreaterThan']) <= float(args['amountLessThan']):
            pass
        else:
            raise InvalidParameter('"amountGreaterThan" is expected to be equal or smaller than "amountLessThan" '
                                   'and positive')

        return args
    if args_length == 1:
        if args.to_dict().get('amountLessThan') and float(args.to_dict().get('amountLessThan')) > 0:
            return args
        elif args.to_dict().get('amountGreaterThan') and float(args.to_dict().get('amountGreaterThan')) > 0:
            return args
        else:
            raise InvalidParameter('the expected parameter name is "amountLessThan" '
                                   'or "amountGreaterThan" with positive values')

    return None


def validate_balance(balance):
    if balance < 0:
        raise InvalidParameter("Update balance with positive values only")
    return balance
