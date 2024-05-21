# big numbers - no problem in python



import re


a = 12345678910111213141516171819120212323242563372828263648473458648563469234
b = 10000000000000000000000000000000

print (a * b)


# append - no (real) limit to the number of items in a list
list = [10,11,12,13]

print (list)

list.append(14)

print (list)

# pop - remove an item
item = list.pop(0)
print(item)
print (list)


while len(list) > 0:
    print (list.pop(), list)

print (list)


# list comprehension
 
list = [1, 5, 2, 9, 8, 6, 5, 7, 10, 2, 3]

even_numbers = [x for x in list if x % 2 == 0]

print (even_numbers)

ssnumbers = [
    "1234567A", "12345678B", "1234", "1234T", "1234567AA", "B12345678A"
]

pps = [n for n in ssnumbers if re.match("^[0-9]{7,8}[A-Z]{1,2}", n)]
print (pps)











