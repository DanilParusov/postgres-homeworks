"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from utils import get_data



with psycopg2.connect(host="localhost",database="north",user="postgres",password="12345") as conn:
    with conn.cursor() as cur:
        for row in get_data("north_data/customers_data.csv"):
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
        for row in get_data("north_data/employees_data.csv"):
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
        for row in get_data("north_data/orders_data.csv"):
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)


conn.close()