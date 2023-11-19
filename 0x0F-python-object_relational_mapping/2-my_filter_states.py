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
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY\
    '{}' ORDER BY id ASC""".format(searched))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
