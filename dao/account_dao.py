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
                return Account(added_acc[0], added_acc[1], added_acc[2], added_acc[3])

    def get_accounts_by_customer_id(self, customer_id, args):

        if args:
            args_length = len(args)
        else:
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
                        balance = account[3]

                        accounts.append(Account(account_id, type_id, currency_id, balance))

                    return accounts
        if args_length == 2:
            amountGreaterThan = args['amountGreaterThan']
            amountLessThan = args['amountLessThan']

            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM accounts as a "
                                "JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                                "WHERE awc.customer_id = %s AND a.balance > %s AND "
                                "a.balance < %s", (customer_id, amountGreaterThan, amountLessThan))

                    accounts = []
                    # iterate over each row of the results
                    for account in cur:
                        account_id = account[0]
                        type_id = account[1]
                        currency_id = account[2]
                        balance = account[3]

                        accounts.append(Account(account_id, type_id, currency_id, balance))

                    return accounts

        elif args_length == 1:
            if 'amountLessThan' in args.keys():
                amountLessThan = args['amountLessThan']
                with pool.connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT * FROM accounts as a "
                                    "JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                                    "WHERE awc.customer_id = %s AND "
                                    "a.balance < %s", (customer_id, amountLessThan))

                        accounts = []
                        # iterate over each row of the results
                        for account in cur:
                            account_id = account[0]
                            type_id = account[1]
                            currency_id = account[2]
                            balance = account[3]

                            accounts.append(Account(account_id, type_id, currency_id, balance))

                        return accounts
            else:
                amountGreaterThan = args['amountGreaterThan']
                with pool.connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT * FROM accounts as a "
                                    "JOIN customers_with_accounts as awc ON a.id = awc.account_id "
                                    "WHERE awc.customer_id = %s AND a.balance > %s", (customer_id, amountGreaterThan))

                        accounts = []
                        # iterate over each row of the results
                        for account in cur:
                            account_id = account[0]
                            type_id = account[1]
                            currency_id = account[2]
                            balance = account[3]

                            accounts.append(Account(account_id, type_id, currency_id, balance))

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
                cur.execute("UPDATE accounts SET type_id = %s, currency_id = %s, balance = %s WHERE id = %s RETURNING *"
                            , (account.get_type_id(), account.get_currency_id(), account.get_balance(),
                               account.get_account_id()))
                account = cur.fetchone()
                if not account:
                    return None
                return Account(account[0], account[1], account[2], account[3])

    def delete_account_by_id(self, account_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts WHERE id = %s RETURNING *", (account_id, ))
                account = cur.fetchone()
                if not account:
                    return None
                return Account(account[0], account[1], account[2], account[3])


    
