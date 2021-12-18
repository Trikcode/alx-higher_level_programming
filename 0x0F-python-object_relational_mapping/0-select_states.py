#!/usr/bin/python3
""" select states """
import MySQLdb
from sys import argv


def select_states():
    """ access database print states """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    select_states()
