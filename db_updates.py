import sqlite3
from Member import Member

filename = "C:\\work\\training\\db\\members.db" 

conn = sqlite3.connect(filename)
cur = conn.cursor()

#sql = "INSERT INTO members (name, email, active, score) VALUES('Fred', 'fred@gmail.com', 1, 10)"

#sql = "UPDATE members SET active = 1 WHERE ID > 2"

sql = "DELETE FROM members WHERE ID = 5"

cur.execute(sql)

conn.commit()
conn.close()

