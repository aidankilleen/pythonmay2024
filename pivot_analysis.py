import sys

from Record import Record

print ("Pivot Analysis")

filename = sys.argv[1]
count = 0

result = {}
colours = set()
products = set()

with open(filename, "r") as file:

    # not using readline - doesn't load 
    # complete file into memory!
    for line in file:

        if count >= 1:
            r = Record(line)

            colours.add(r.colour)
            products.add(r.product)

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

# file is automatically closed at the end of the
# with block

# sort the products
sorted_products = sorted(products)
sorted_colours = sorted(colours)

# print the top row
print("\t", end = "")
for colour in sorted_colours:
    print (colour, end="\t")
print ("\n", end = "")


# print one row for each product
for product in sorted_products:
    print (product, end="\t")
    for colour in sorted_colours:
        if colour in result[product]:
            print (result[product][colour], end="\t")
        else: 
            print ("\t", end = "")


    print("")

