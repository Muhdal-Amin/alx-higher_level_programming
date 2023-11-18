#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_usa"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    #script arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        database=database_name,
    )

    cursor = db.cursor
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    cursor.close()
    db.close()
