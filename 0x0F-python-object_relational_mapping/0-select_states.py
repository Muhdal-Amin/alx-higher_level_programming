#!/usr/bin/python3
"""A script that selects states from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
