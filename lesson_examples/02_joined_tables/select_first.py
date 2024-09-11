import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('database/salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
    SELECT ROUND(AVG(payments.total), 0) AS Average_Payments, employees.post
    FROM payments
    JOIN employees ON employees.id = payments.employee_id
    GROUP BY employees.post;
"""

print(execute_query(sql))
