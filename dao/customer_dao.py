from model.customer import Customer
from utility.db_connection import pool


class CustomerDao:
    # CRUD operations
    # Create - insert a new customer into our "database"
    # Read - Retrieve a customer or users from our "database"
    # Update - Update a customer in our "database"
    # Delete - Delete a customer in our "database"

    def get_all_customers(self):

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                my_list_of_customer_objs = []
                # iterate over each row of the results
                for customer in cur:
                    customer_id = customer[0]
                    first_name = customer[1]
                    last_name = customer[2]
                    date_of_birth = customer[3]
                    customer_since = customer[4]
                    email = customer[5]
                    postal_code = customer[6]
                    unit_no = customer[7]
                    mobile_phone = customer[8]

                    my_list_of_customer_objs.append(Customer(customer_id,
                                                             first_name,
                                                             last_name,
                                                             date_of_birth,
                                                             customer_since,
                                                             email,
                                                             postal_code,
                                                             unit_no,
                                                             mobile_phone))

                return my_list_of_customer_objs

    def get_customer_by_id(self, customer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * "
                            "   FROM customers "
                            "   WHERE id = %s", (customer_id,))

                cust = cur.fetchone()
                if not cust:
                    return None

                customer_id, first_name, last_name, date_of_birth, customer_since, \
                email, postal_code, unit_no, mobile_phone = cust  # destructuring a tuple

                return Customer(customer_id, first_name, last_name, date_of_birth,
                                customer_since, email, postal_code, unit_no, mobile_phone)

    def add_customer(self, cust):

        first_name = cust.get_first_name()
        last_name = cust.get_last_name()
        date_of_birth = cust.get_date_of_birth()
        email = cust.get_email()
        postal_code = cust.get_postal_code().replace(" ", "")  # ensure postal code does not contain spaces
        unit_no = cust.get_unit_no()
        mobile_phone = cust.get_mobile_phone()

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (first_name, last_name, "
                            "date_of_birth, customer_since, email, postal_code, "
                            "unit_no, mobile_phone) VALUES (%s, %s, %s, "
                            "current_date, %s, %s, %s, %s) RETURNING *",
                            (first_name, last_name, date_of_birth, email,
                             postal_code, unit_no, mobile_phone)
                            )
                inserted_record = cur.fetchone()
                if not inserted_record:
                    return None
                customer_id, first_name, last_name, date_of_birth, customer_since, email, postal_code, \
                unit_no, mobile_phone = inserted_record
                return Customer(customer_id, first_name, last_name, date_of_birth,
                                customer_since, email, postal_code, unit_no,
                                mobile_phone)

    def update_customer_by_id(self, cust):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE customers SET last_name = %s, email = %s, postal_code = %s, unit_no = %s,"
                            "mobile_phone = %s WHERE id = %s RETURNING *",
                            (cust.get_last_name(), cust.get_email(), cust.get_postal_code(),
                             cust.get_unit_no(), cust.get_mobile_phone(),
                             cust.get_customer_id()))
                u_cust = cur.fetchone()
                if not u_cust:
                    return None

                return Customer(u_cust[0], u_cust[1], u_cust[2], u_cust[3], u_cust[4],
                                u_cust[5], u_cust[6], u_cust[7], u_cust[8])

    def delete_customer_by_id(self, customer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers WHERE id = %s RETURNING *",
                            (customer_id,))
                return cur.fetchone()
