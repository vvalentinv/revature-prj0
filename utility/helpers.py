import re
from utility.db_connection import pool
from exception.invalid_parameter import InvalidParameterError


def check_date(date):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_date - interval '16 year' <= %s;", (date,))
            if cur.fetchone()[0]:
                raise InvalidParameterError("Minimum Customer age must be 16 years-old")
            return True


def validate_name(string):
    if not string:
        return None
    if len(string) < 2:
        raise InvalidParameterError("Names must have at least 2 letters")
    if " " in string:
        raise InvalidParameterError("Username cannot contain spaces")
    return True


def validate_email(string):
    reg_email = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(reg_email, string):
        raise InvalidParameterError("accepted email address format is <username>@<company>.<domain>")
    return True


def validate_postal_code(string):
    if not 4 < len(string.replace(" ", "")) < 7:
        raise InvalidParameterError("Postal code length must be equal to 5 or 6 without any space")
    return True


def validate_phone(string):
    reg_phone = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
    if not re.match(reg_phone, string):
        raise InvalidParameterError("mobile phone format 555-555-5555")
    return True

def validate_args(args):
    args_length = 0
    if args:
        args_length = len(args)
    if args_length == 2:
        if 'amountLessThan' in args.keys():
            pass
        else:
            raise InvalidParameterError('the expected parameter name is "amountLessThan" ')
        if 'amountGreaterThan' in args.keys():
            pass
        else:
            raise InvalidParameterError('the expected parameter name is "amountGreaterThan" ')
        if 0 <= args['amountGreaterThan'] <= args['amountLessThan']:
            pass
        else:
            raise InvalidParameterError(' "amountGreaterThan" is expected to be equal or smaller than "amountLessThan" and positive')

        return args
    if args_length == 1:
        if args.keys()[0] in ('amountGreaterThan', 'amountLessThan'):
            if args.keys()[0] == 'amountGreaterThan' and args['amountGreaterThan'] >= 0:
                return args
            elif args.keys()[0] == 'amountGreaterThan' and args['amountGreaterThan'] < 0:
                raise InvalidParameterError(' "amountGreaterThan" is expected to have a positive value')
            elif args.keys()[0] == 'amountLessThan' and args['amountLessThan'] >= 0:
                return args
            else:
                raise InvalidParameterError(' "amountLessThan" is expected to have a positive value')
        else:
            raise InvalidParameterError('the expected parameter name is "amountLessThan" '
                                        'or "amountGreaterThan"')
    return None



