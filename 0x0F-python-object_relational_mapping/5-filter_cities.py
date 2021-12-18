#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "INNER JOIN states "
                "ON states.id=cities.state_id "
                "WHERE states.name= %s "
                "ORDER BY cities.id ",
                (argv[4], ))
    query_rows = cur.fetchall()
    list1 = []
    for row in query_rows:
        list1.append(row[1])
    result = ', '.join(list1)
    print(result)
    cur.close()
    db.close()
