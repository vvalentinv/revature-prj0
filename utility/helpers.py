from utility.db_connection import pool


def check_date(date):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_date - interval '16 year' <= %s;", (date,))
            if not cur.fetchone()[0]:
                return True
            return False
