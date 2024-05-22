import sys

from Record import Record

print ("Pivot Analysis")

filename = sys.argv[1]
count = 0

result = {}
colours = set()

with open(filename, "r") as file:

    # not using readline - doesn't load 
    # complete file into memory!
    for line in file:

        if count >= 1:
            r = Record(line)

            colours.add(r.colour)

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

# print the top row
print("\t", end = "")
for colour in colours:
    print (colour, end="\t")
print ("\n", end = "")

# print one row for each product
for product in result:
    print (product, end="\t")
    for colour in colours:
        if colour in result[product]:
            print (result[product][colour], end="\t")
        else: 
            print ("\t", end = "")


    print("")

