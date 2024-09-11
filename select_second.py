import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('database/salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
    SELECT COUNT(*) AS employee, companies.company_name
    FROM employees
    LEFT JOIN companies ON companies.id = employees.company_id
    GROUP BY companies.company_name
"""

print(execute_query(sql))
