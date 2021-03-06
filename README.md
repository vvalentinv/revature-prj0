# Project 0: RESTful API

Due Date: Friday, July 8th

## Project Description
You are developing a simple API for a bank.

Leveraging Python, create a RESTful API application that supports two main resources: customers and accounts.

* Customer: a particular customer of the bank
* Account: a client can have multiple bank accounts (ex. 2 checking accounts, 3 savings accounts)

### Technologies
1. Python
2. Flask
3. Psycopg
4. PyTest
5. PostgreSQL
6. MagicMock

## Requirements

### Endpoint Requirements
The following endpoints and their respective verbs should support the operations as described. In the HTTP response, use appropriate status codes (as specific as possible) and response bodies where applicable.

- `POST /customers`: Creates a new customer~~
- `GET /customers`: Gets all customers~~
- `GET /customer/{customer_id}`: Get customer with an id of X (if the customer exists)~~
- `PUT /customer/{customer_id}`: Update customer with an id of X (if the customer exists)~~
- `DELETE /customer/{customer_id}`: Delete customer with an id of X (if the customer exists)~~
- `POST /customer/{customer_id}/accounts`: Create a new account for a customer with id of X (if customer exists)~~
- These two should be the same endpoint (you will need logic for whether the query parameters exist):
    - `GET /customer/{customer_id}/accounts`: Get all accounts for customer with id of X (if customer exists)~~
    - `GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300`: Get all accounts for customer id of X with balances between Y and Z (if customer exists)~~
- `GET /customer/{customer_id}/account/{account_id}`: Get account with id of Y belonging to customer with id of X (if customer and account exist AND if account belongs to customer)~~
- `PUT /customer/{customer_id}/account/{account_id}`: Update account with id of Y belonging to customer with id of X (if customer and account exist AND if account belongs to customer)~~
- `DELETE /customer/{customer_id}/account/{account_id}`: Delete account with id of Y belonging to customer with id of X (if customer and account exist AND if account belongs to customer)

### General Requirements
- Python
- Users of the application should be able to interact with it through a RESTful API utilizing HTTP
- 3 layered architecture (n-tiered architecture)
    - Controller (presentation) layer
    - Service (business logic) layer
    - Data Access layer (DAO aka Data Access Object layer)
- Unit testing
    - 80-90% test coverage for the **service layer** using PyTest
        - Utilize MagicMock in order to mock DAO dependencies
- Create a SQL script that will create a table schema and populate some data for your application
- Utilize Psycopg in the application for data persistence
    - Must utilize the DAO design pattern
    - PostgreSQL

### Stretch Goals
Remember that the above requirements are the minimum viable product (MVP). You can always look into adding more

Here are some ideas:
- Run the application on a docker image
- Deploy the application to an AWS EC2 instance
- Use at least 1 stored procedure w/ Postgres
- Additional resources and RESTful endpoints (in addition to the customers and accounts resources in the main requirements)


## Install and run

1. Clone the repository or download the zip archive
2. Create a PostgreSQL database(check the utility package for the SQL) and fill in the .env.example file with that db info and rename the file to .env
3. Open a Git Bash session in the project's location and build the virtual environment using "python -m venv ./venv"
4. Run "pip install -r requirements.txt" to install all project dependencies
5. To start it either open in your IDE of choice that supports it or "python app.py"
6. To run the tests use "coverage run --source=service --module pytest --verbose test && coverage report --show-missing
" in Git Bash session in project directory
7. Optionally the Postman collection for this api can be imported from the utility package