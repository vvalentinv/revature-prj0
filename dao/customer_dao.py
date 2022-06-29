from model.customer import Customer
from dotenv import dotenv_values
from utility.db_connection import pool

config = dotenv_values(".env")


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
                # iterate over each row of the users table
                for customer in cur:
                    # print(customer)
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

