# Building Block #1 - Comments
#
# This is a comment

# Building Block #2 - Variables
name = "Aidan"
a = 10
b = 20

print (name)
name = "Fred"
print (name)

# python is not particularly type-safe, you can change the type of a 
# variable if you like
a = "ten"
print (a)

# Building block #3 - expressions
a = 10

answer = a + b
print ("The answer is ")
print (answer)

# aside - strings
# print ("The answer is " + answer)
print ("The answer is " + str(answer))

# f-strings for formatting string are better than concatenation
print (f"The answer is { answer }")

print (f"{ a } + { b } = { a + b }")


# Building block # 4 = lists / arrays
list = [1, 2, 3, 4, 5]

print (list)
print (list[1]) # arrays are zero based list[0] is the first item
print (len(list))


stuff = [1, "one", 1.1, [1,2,3]]

print (stuff[0])
print (stuff[1])
print (stuff[2])
print (stuff[3])

#2 dimensional arrays are possible
print (stuff[3][2])
# print (stuff[5]) # out of bounds - causes a runtime error


#Building block #5 - loops
items = [1, 4, 3, 2, 6, 5, 7]
i = 0
# in python, unlike other languages the whitespace indent is 
# part of the syntax

while i < len(items):
    print (items[i])
    i = i + 1

print ("==============================")

# for each loop
for item in items:
    print (item)


# Building Block #6 - Conditions
    
numbers = [1, 5, 4, 7, 6, 9, 8, 10]

for number in numbers:
    if number % 2 == 0:
        print (f"{ number } is even")
    else:
        print (f"{ number } is odd")

# multiple conditions
for number in numbers:
    if number <= 4:
        print (f"{ number } is small")
    elif number <= 7:
        print (f"{ number } is medium")
    else:
        print (f"{ number } is large")

# ternary operator
# put a condition on a single line

for number in numbers:
    print (f"{ number } is { "odd" if number % 2 == 1 else "even" }")


# Building Block #7 - functions

# 7a - built in functions
print("print is a function") 
print("the value is " + str(answer))
print("the length is " + str(len(numbers)))


#range creates a list
numbers = range(10)

for i in numbers:
    print (i)

# traditional for loop
# for (i = 0; i<10; i++) - c-style for loop
# this is the python implementation: 
for i in range(10):
    print (i)

#7b - user defined functions
print ("user defined function")

# define the function
def my_function():
    print ("Custom function")

# call the function
my_function()


# functions take parameters
# functions can return a value

# my_add(1, 2) # you can't call a function before it is defined

def my_add(x, y):
    return x + y

a = 10
b = 20

answer = my_add(a, b)
print (f"The answer is { answer }")

# Building Block #8 - Objects
# python is an object oriented programming language
list = [1,3,2,4,3,5,9]























































