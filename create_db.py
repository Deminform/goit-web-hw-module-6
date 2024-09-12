import sqlite3


def create_db():
    with open('sql_files/db_initializer.sql', 'r') as file:
        sql = file.read()

    with sqlite3.connect('database/school.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == '__main__':
    create_db()
