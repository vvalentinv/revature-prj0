from model.account import Account
from utility.db_connection import pool


class AccountDao:

    def add_account_by_customer_id(self, account, customer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (type_id, currency_id, balance)"
                            "VALUES(%s, %s, %s) RETURNING *", (account.get_type_id(),
                                                               account.get_currency_id(),
                                                               account.get_balance()))
                added_acc = cur.fetchone()
                cur.execute("INSERT INTO customers_with_accounts (account_id, customer_id)"
                            "VALUES (%s, %s) RETURNING *", (added_acc[0], customer_id))
                return added_acc
