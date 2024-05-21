from random import randint, random

from Member import Member




def test_function():
    print ("test function")


test_function()

def greet(name, greeting):
    print (f"{ greeting } { name }")

greet("Bonjour", "Aidan")

# you can change the order by specifying which parameter you are providing
# these are called "keyword parameters"
greet(greeting="Hello", name="Fred")

# you can provide a default value for a parameter
# parameters with defaults become optional
def welcome(name = "", message = "Welcome"):
    print (f"{ message } { name }")

welcome("Alice", "Failte")
welcome("Bob")

welcome()

# complex functions with a lot of parameters
# often have defaults for all the parameters
# an you just provide the parameters you need
# in the example below - d
def complex_function(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    print ("something complex")

complex_function(d=99)


a = 10
b = 20
answer = 30

print (a, end=" ")
print (b, end=" ")
print (answer, end=" ")

print ("*" * 25)
member = Member()

print (member)

member =Member(name="Alice", email="alice@gmail.com")

print (member)




















