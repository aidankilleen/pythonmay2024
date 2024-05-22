# this is going to write some test records to a CSV file

import random
import sys

if len(sys.argv) != 3:
    print ("Please supply a filename and count")
    exit()


csv_filename = sys.argv[1]
count = int(sys.argv[2])

#csv_filename = "C:\\work\\training\\db\\salesdata.csv"

names = ['Alice', 'Bob', 'Carol', 'Dan', 'Eve', 'Fred', 'Ger', 'Harriet']
colours = ['red', 'green', 'blue', 'orange', 'pink', 'purple', 'black', 'white']
products = ['pen', 'pencil', 'eraser', 'paper', 'card', 'paint']

with open(csv_filename, "w") as file:

    file.write('id,name,product,colour,quantity\n')

    for id in range(1, count+1):
        name = random.choice(names)
        product = random.choice(products)
        colour = random.choice(colours)

        quantity = random.randint(1,100)

        file.write(f"{id},{name},{product},{colour},{quantity}\n")


