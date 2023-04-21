#!/usr/bin/python3
"""Select from states table module."""
import MySQLdb
import sys


if __name__ == "__main__":
    connect = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3],
                                charset="utf8"
                             )
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    response = cursor.fetchall()
    for row in response:
        print(row)
    cursor.close()
    connect.close()
