from utility.db_connection import pool
from exception.invalid_parameter import InvalidParameterError


def check_date(date):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_date - interval '16 year' <= %s;", (date,))
            res = cur.fetchone()
            print("999999999999999999", res)
            if res[0]:
                raise InvalidParameterError("Minimum Customer age must be 16 years-old")
            return True


def validate_name(string):
    if len(string) < 2:
        raise InvalidParameterError("Names must have at least 2 letters")
    elif " " in string:
        raise InvalidParameterError("Username cannot contain spaces")
