
filename = "test.csv"
with open(filename, "r") as file:

    # not using readline - doesn't load 
    # complete file into memory!
    for line in file:
        print (line)


# by using with - the close function 
# is automatically called when the with 
# block ends


