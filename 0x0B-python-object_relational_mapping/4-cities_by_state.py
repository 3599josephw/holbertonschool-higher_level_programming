#!/usr/bin/python3
"""Lists cities and states"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities LEFT JOIN states ON states.id = cities.state_id")

    for row in cur.fetchall():
        print(row)

    db.close()
