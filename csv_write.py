import sqlite3
from Member import Member

db_filename = "C:\\work\\training\\db\\members.db" 
csv_filename = "C:\\work\\training\\db\\members.csv"

conn = sqlite3.connect(db_filename)
cur = conn.cursor()
sql = "SELECT * FROM members"

# file mode w - will overwrite
# file mode a - will append
with open(csv_filename, "a") as file:

    file.write("id,name, email, active, score\n")
    for row in cur.execute(sql):
        #write to the csv file
        # file.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n")
        
        output = ",".join(str(item) for item in row) # use a list comprehension instead
        file.write(f"{output}\n")

conn.close()

