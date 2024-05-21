filename = "test.csv"

# first pass

fd = open(filename, "r")

lines = fd.readlines()

for line in lines:
    print (line)

fd.close()





