
from  sqlite4  import  SQLite4

# Init database object, singleton pattern restricts multiple objects per db
filename = "C:\\work\\training\\db\\members.db" 

database = SQLite4(filename)
# Connect to db and creates execution thread
database.connect()

result = database.select("members")

print (result)

database.disconnect()

