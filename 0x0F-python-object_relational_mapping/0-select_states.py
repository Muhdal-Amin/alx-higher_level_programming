#!/usr/bin/python3
"""A script that lists all states from the database"""
import sys
import MySQLdb


def select_states():
    """Gets states from the databse"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database
                           )

    cursor = db.cursor
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states()
