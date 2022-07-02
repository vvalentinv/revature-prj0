DROP TABLE IF EXISTS currencies CASCADE;
DROP TABLE IF EXISTS account_types CASCADE;
DROP TABLE IF EXISTS customers_with_accounts CASCADE;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS customers;


CREATE TABLE currencies (
	id SERIAL PRIMARY KEY,
	currency_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE account_types (
	id SERIAL PRIMARY KEY,
	type_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE accounts(
	id SERIAL PRIMARY KEY,
	type_id INT NOT NULL,
	currency_id INT NOT NULL,
	balance BIGINT NOT NULL CHECK(balance > 0),
	CONSTRAINT fk_account_type
  		FOREIGN KEY (type_id) REFERENCES "account_types" (id),
  	CONSTRAINT fk_currency
  		FOREIGN KEY (currency_id) REFERENCES "currencies" (id)
);

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50)  NOT NULL,
	last_name VARCHAR(50)  NOT NULL,
	date_of_birth DATE NOT NULL,
	customer_since DATE NOT NULL,
	email VARCHAR(50) NOT NULL,
	postal_code VARCHAR(50) NOT NULL,
	unit_no VARCHAR(50) NOT NULL,
	mobile_phone VARCHAR(50) NOT NULL

);

CREATE TABLE customers_with_accounts(
	account_id INT NOT NULL,
	customer_id INT NOT NULL,
	PRIMARY KEY (account_id, customer_id)
);


-- INSERTS;

INSERT INTO currencies (currency_name)
	VALUES ('CAD'),
			('USD'),
			('EURO');
		
INSERT INTO account_types (type_name)
	VALUES ('SAVINGS'),
			('CHEQUING');	
		
INSERT INTO accounts (type_id, currency_id, balance)
	VALUES 	(1,1,5),
			(1,2,5),
			(2,3,5);
	
INSERT INTO customers (first_name, last_name, date_of_birth, customer_since, email, postal_code, unit_no, mobile_phone)
	VALUES 	('John','Doe','1908-01-01','2000-01-01','a@a.ca', 'M2J 1M5', '555', '555-555-500'),
			('Jane','Doe','1908-01-01','1908-01-02','a@a.ca', 'M2J 1M5', '555', '555-555-501'),
			('test','user3','1908-01-01','1908-01-03','a@a.ca', 'M2J 1M5', '555', '555-555-502');

		

SELECT * FROM customers_with_accounts;		
		
INSERT INTO customers_with_accounts (account_id, customer_id)
	VALUES 	(3,2) RETURNING *;

		Select current_date - interval '16 year' <= '2005-01-01';

select current_date;

SELECT * FROM accounts as aJOIN customers_with_accounts as awc ON a.id = awc.account_idWHERE awc.customer_id = 2 AND  a.balance > 5 AND a.balance < 100000 ;