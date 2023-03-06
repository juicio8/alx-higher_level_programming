#!/usr/bin/python3
# script that lists all states with a name
# starting with N (upper N) from the database hbtn_0e_0_usa:
"""
    lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa:
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost:3306",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[0] == 'N']
    cur.close()
    db.close()
