#!/usr/bin/python3
"""Lists all rows from the states table"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.name FROM cities INNER JOIN
states ON cities.state_id = states.id AND states.name = '%s'""" % sys.argv[4])

    result = cur.fetchall()
    flag = 1

    for row in result:
        print(row[0], end="")
        if flag != len(result):
            print(", ", end="")
        else:
            print("")
        flag += 1

    db.close()
