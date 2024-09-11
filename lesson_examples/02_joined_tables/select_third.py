import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('database/salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
    SELECT companies.company_name, employees.employee, employees.post, payments.total
    FROM companies
        LEFT JOIN employees ON employees.company_id = companies.id
        LEFT JOIN payments ON payments.employee_id = employees.id
    WHERE payments.total > 5000
        AND payments.date_of BETWEEN '2024-07-10' AND '2024-07-20'
"""

print(execute_query(sql))
