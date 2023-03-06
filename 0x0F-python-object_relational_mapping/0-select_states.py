#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa:
"""
    lists all states from the database hbtn_0e_0_usa:
   
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost:3306",
                         user='root', passwd='root', db='hbtn_0e_0_usa')
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
