import sqlite3


def create_db():
    with open('database/school.sql', 'r') as file:
        sql = file.read()

    with sqlite3.connect('database/salary.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == '__main__':
    create_db()
