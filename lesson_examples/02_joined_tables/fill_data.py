from datetime import datetime
import faker
from random import randint, choice
import sqlite3


NUMBER_COMPANIES = 3
NUMBER_EMPLOYEES = 30
NUMBER_POST = 5


def generate_fake_data(number_companies, number_employees, number_post):
    fake_companies = []
    fake_employees = []
    fake_posts = []
    fake_data = faker.Faker()

    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts


# companies, employees, posts = generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYEES, NUMBER_POST)
# print(companies)
# print(employees)
# print(posts)


def prepare_data(companies, employees, posts):
    for_companies = []
    for company in companies:
        for_companies.append((company, ))

    for_employees = []
    for emp in employees:
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    for_payments = []
    for month in range(1, 12 + 1):
        payment_date = (datetime(2024, month, randint(10, 20))).strftime('%Y-%m-%d %H:%M:%S')
        for emp in range(1, NUMBER_EMPLOYEES + 1):
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments


def insert_data_to_db(companies, employees, payments):
    with sqlite3.connect('database/salary.db') as con:
        cur = con.cursor()

        sql_to_companies = 'INSERT INTO companies(company_name) VALUES (?)'
        cur.executemany(sql_to_companies, companies)

        sql_to_employees = 'INSERT INTO employees(employee, post, company_id) VALUES (?, ?, ?)'
        cur.executemany(sql_to_employees, employees)

        sql_to_payments = 'INSERT INTO payments(employee_id, date_of, total) VALUES (?, ?, ?)'
        cur.executemany(sql_to_payments, payments)


if __name__ == '__main__':
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYEES, NUMBER_POST))
    insert_data_to_db(companies, employees, posts)
