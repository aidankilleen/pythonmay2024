import sqlite3
from Member import Member

filename = "C:\\work\\training\\db\\members.db" 

conn = sqlite3.connect(filename)
cur = conn.cursor()
sql = "SELECT * FROM members"
members = []
for row in cur.execute(sql):
    #member = Member(row[0], row[1], row[2], row[3], row[4])
    member = Member(*row)   # you can unpack the tuple into individual arguments using *
    members.append(member)

conn.close()

for member in members:
    print (member)