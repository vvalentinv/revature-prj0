from model.account import Account
from utility.db_connection import pool


class AccountDao:

    def add_account_by_customer_id(self, account, customer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (type_id, currency_id, balance_in_cents)"
                            "VALUES(%s, %s, %s) RETURNING *", (account.get_type_id(),
                                                               account.get_currency_id(),
                                                               account.get_balance_in_cents()))
                added_acc = cur.fetchone()
                cur.execute("INSERT INTO customers_with_accounts (account_id, customer_id)"
                            "VALUES (%s, %s) RETURNING *", (added_acc[0], customer_id))
                return Account(added_acc[0], added_acc[1], added_acc[2], added_acc[3])

    def get_accounts_by_customer_id(self, customer_id):

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts as a "
                            "JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                            "WHERE awc.customer_id = %s",
                            (customer_id,))
                accounts = []
                # iterate over each row of the results
                for account in cur:
                    account_id = account[0]
                    type_id = account[1]
                    currency_id = account[2]
                    balance_in_cents = account[3]

                    accounts.append(Account(account_id, type_id, currency_id, balance_in_cents))

                return accounts

    def get_accounts_by_customer_id_agt_alt(self, customer_id, agt, alt):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts as a JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                            "WHERE awc.customer_id =%s AND a.balance_in_cents > %s AND a.balance_in_cents < %s", (customer_id,
                                                                                                agt, alt))
                accounts = []
                # iterate over each row of the results
                print(customer_id)
                for account in cur:

                    account_id = account[0]
                    type_id = account[1]
                    currency_id = account[2]
                    balance_in_cents = account[3]

                    accounts.append(Account(account_id, type_id, currency_id, balance_in_cents))

                return accounts

    def get_accounts_by_customer_id_alt(self, customer_id, alt):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts as a "
                            "JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                            "WHERE awc.customer_id = %s AND "
                            "a.balance_in_cents < %s", (customer_id, alt))

                accounts = []
                print(customer_id)
                # iterate over each row of the results
                for account in cur:
                    account_id = account[0]
                    type_id = account[1]
                    currency_id = account[2]
                    balance_in_cents = account[3]

                    accounts.append(Account(account_id, type_id, currency_id, balance_in_cents))

                return accounts

    def get_accounts_by_customer_id_agt(self, customer_id, agt):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts as a "
                            "JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                            "WHERE awc.customer_id = %s AND a.balance_in_cents > %s", (customer_id, agt))

                accounts = []
                print(customer_id)
                # iterate over each row of the results
                for account in cur:
                    account_id = account[0]
                    type_id = account[1]
                    currency_id = account[2]
                    balance_in_cents = account[3]

                    accounts.append(Account(account_id, type_id, currency_id, balance_in_cents))

                return accounts

    def get_account_by_id(self, account_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))
                account = cur.fetchone()
                if not account:
                    return None
                return Account(account[0], account[1], account[2], account[3])

    def get_customer_account_by_account_id(self, customer_id, account_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers_with_accounts WHERE account_id = %s and customer_id = %s",
                            (account_id, customer_id))
                account_customer_link = cur.fetchone()
                if not account_customer_link:
                    return None
                return account_customer_link

    def update_account_by_id(self, account):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE accounts SET type_id = %s, currency_id = %s, balance_in_cents = %s "
                            "WHERE id = %s RETURNING *", (account.get_type_id(), account.get_currency_id(),
                                                          account.get_balance_in_cents(), account.get_account_id()))
                account = cur.fetchone()
                if not account:
                    return None
                return Account(account[0], account[1], account[2], account[3])

    def delete_account_by_id(self, account_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts WHERE id = %s RETURNING *", (account_id,))
                account = cur.fetchone()
                if not account:
                    return None
                return Account(account[0], account[1], account[2], account[3])

    def check_for_joined_accounts_by_id(self, account_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM customers_with_accounts WHERE account_id = %s",
                            (account_id,))
                assoc_num = cur.fetchone()
                if not assoc_num[0]:
                    return None
                elif assoc_num[0] >= 2:
                    return True
                else:
                    return False

    def delete_joined_association(self, account_id, customer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers_with_accounts "
                            "WHERE account_id = %s AND customer_id = %s RETURNING *", (account_id, customer_id))
                assoc = cur.fetchone()
                if not assoc:
                    return None
                return assoc[0], assoc[1]
