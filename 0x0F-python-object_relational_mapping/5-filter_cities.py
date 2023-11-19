#!/usr/bin/python3
"""A script that lists all cities in state from the database"""
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
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (state_name,))

    rows = cur.fetchall()
    result = []

    for row in rows:
        for col in row:
            result.append(col)
    print(', '.join(result))
    cur.close()
    db.close()
