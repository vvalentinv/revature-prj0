DROP TABLE IF EXISTS customers_with_accounts;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS currencies;
DROP TABLE IF EXISTS account_types;


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
	VALUES 	(1,1,100),(2,1,500),(1,3,5000),
			(2,1,100),(2,2,500),(2,3,5000),
			(1,1,100),(2,2,500),(1,3,5000),
			(2,3,50000);
	
INSERT INTO customers (first_name, last_name, date_of_birth, customer_since, email, postal_code, unit_no, mobile_phone)
	VALUES 	('John','Doe','1980-01-01','2000-01-01','jd@a.ca', 'M2J 1M5', '550', '555-555-5000'),
			('Jane','Doe','1981-01-01','2003-01-02','j@a.ca', 'M2J 1M5', '551', '555-555-5001'),
			('Johny','Doe','2000-01-01','2020-01-03','jhy@a.ca', 'M2J 1M5', '553', '555-555-5003'),
			('John1','Doe1','1980-01-01','2000-01-01','jd@a.ca', 'M2J 1M5', '554', '555-555-5004'),
			('Jane1','Doe1','1981-01-01','2003-01-02','j@a.ca', 'M2J 1M5', '555', '555-555-5005'),
			('Johny1','Doe1','2000-01-01','2020-01-03','jhy@a.ca', 'M2J 1M5', '556', '555-555-5006'),
			('John2','Doe','1980-01-01','2000-01-01','jd@a.ca', 'M2J 1M5', '557', '555-555-5007'),
			('Jane2','Doe','1981-01-01','2003-01-02','j@a.ca', 'M2J 1M5', '558', '555-555-5008'),
			('Johny2','Doe','2000-01-01','2020-01-03','jhy@a.ca', 'M2J 1M5', '559', '555-555-5009');
		
INSERT INTO customers_with_accounts (account_id, customer_id)
	VALUES 	(1,1),(2,1),(3,1),(4,2),(5,2),(4,1),(5,1),(6,1),
			(6,2),(7,3),(8,3),(9,3),(10,4);

SELECT * FROM accounts;
SELECT * FROM customers;
SELECT * FROM customers_with_accounts;

SELECT current_date - interval '16 year' <= '2008-01-01';


SELECT a.id as acc_id, at2.type_name as account_type, cur.currency_name as currency,
		a.balance, CONCAT_WS(', ', c.last_name,c.first_name) as name, c.id as cust_id
	FROM accounts as a	JOIN account_types at2 ON a.type_id = at2.id
	JOIN currencies cur ON a.currency_id = cur.id
	JOIN customers_with_accounts awc ON a.id = awc.account_id
	JOIN customers c ON awc.customer_id = c.id  	WHERE awc.account_id= 4;

  SELECT * FROM accounts as a 
  	JOIN customers_with_accounts as awc ON a.id = awc.account_id
  	WHERE awc.account_id = 4 ;
