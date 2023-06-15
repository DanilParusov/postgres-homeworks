-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
    title varchar(100) NOT NULL,
	birth_day varchar(50),
    notes text
);

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(50)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(20) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
    order_date date,
	ship_city varchar(50)
);