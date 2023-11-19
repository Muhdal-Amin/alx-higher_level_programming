#!/usr/bin/python3
"""A script that takes in an argument and displays values in the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY\
    '{}' ORDER BY id ASC""".format(state_name_searched))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
