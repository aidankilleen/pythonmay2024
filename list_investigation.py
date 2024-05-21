print ("List / Tuple Investigation")


item_list = [1, 5, 3, 7, 9, 10]

for item in item_list:
    print (item)

print ("=====================")

item_tuple = (10, 6, 4, 5, 2, 9)

for item in item_tuple:
    print (item)

# tuple is immutable i.e. you can't change it
item_list[0] = 999
#item_tuple[0] = 999

# why is this useful / significant?

# use 1 - return multiple results from a function
def process_list(list):
    sum = 0
    for item in list:
        sum = sum + item

    average = sum / len(list)
    
    return (sum, average)


list = [1,2,3,4,5]

result = process_list(list)

print (f"sum: { result[0] }")
print (f"average: { result[1] }")

# assigning a tuple to a tuple will fill in the variables on the left - s and a
(s, a) = process_list(list)

print (f"sum: { s }")
print (f"average: { a }")



# swap two variables
# without needing a third temporary variable

a = 10
b = 20

print (f"a = { a } b = { b }")

(a, b) = (b, a)

print (f"a = { a } b = { b }")

print (item_list)
print (item_tuple)

# extracting items from a list
(u, v, w, x, y, z) = item_tuple

print (u)
print (v)
print (w)
print (x)
print (y)
print (z)

# extracting some items
(item1, item2, *rest) = item_tuple
print (item1)
print (item2)
print (rest)


print ("==========================")
# negative index
list = [1, 3, 2, 6, 5, 4, 9, 10]

print (list[0])
print (list[-1])    # negative index starts from the end
print (list[-2])


subset = list[1:4]
print (subset)

subset = list[4:]
print (subset)

subset = list[:4]
print (subset)

# clone the list by leaving out the numbers
copy = list[:]
print(copy)

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#r = range(0, 10)

print (r)
copy = r[1:9:2]     # start:end:step
print (copy)






