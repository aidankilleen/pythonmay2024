import sys

from Record import Record

print ("Pivot Analysis")

filename = sys.argv[1]
count = 0

result = {}

with open(filename, "r") as file:

    # not using readline - doesn't load 
    # complete file into memory!
    for line in file:

        if count >= 1:
            r = Record(line)
            if r.product in result:
                # subsequent time this product is encountered
                # check if there is already an entry for this colour
                if r.colour in result[r.product]:
                    # subsequent time this colour found for this product
                    # add the quantity to the entry 
                    result[r.product][r.colour] += r.quantity
                else:
                    # first time this colour found for this product
                    # create an entry for the colour and 
                    # set to the quantity
                    result[r.product][r.colour] = r.quantity
            else:
                # first time this product is encountered
                # create a dictionary with an entry for the colour
                # set to the quantity
                result[r.product] = {
                    r.colour: r.quantity
                }

        count +=1

print (result)
