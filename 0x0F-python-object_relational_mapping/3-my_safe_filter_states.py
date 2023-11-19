#!/usr/bin/python3
"""A script that is safe from SQL injection"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (state_name))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
