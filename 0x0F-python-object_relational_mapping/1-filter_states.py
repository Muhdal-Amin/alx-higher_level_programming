#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    # script arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        database=database_name,
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM state WHERE name LIKE BINARY\
     'N%'ORDER BY id ASC ")

    myresults = cursor.fetchall()

    for x in myresult:
        print(x)

    cursor.close()
    db.close()
