from random import randint
print ("Exception Investigation")
a = 10
b = 0
list = [1, 2, 3, 4]
number = "ninety nine"
answer = 0
r = randint(1, 4)
try:
    if r == 1:
        answer = int(number)
    elif r ==2:
        answer = list[4]
    elif r == 3:
        answer = a / b
    else:
        answer = 42 # no error occurred
except ZeroDivisionError:
    print ("you can't divide by zero")
    answer = 0
except ValueError:
    print (f"{ number } is not a number that can be converted")    
    answer = 99
except:
    print ("some other error occurred")    
finally:
    # this code gets run no matter what
    print (f"The answer is { answer }")

print ("finished")






# Exception Handling
# C++ / Java / C# and python
# try:
#     DoSomething()
#     DoSomethingElse()
# except NetworkError:
#     # all errors are handled here
# except FileError:
#     #
# except UserError:
#     #
# finally:
#     #

# print ("it worked")









# tradition c-style defensive programming
# glass is half empty approach
# r = DoSomething()
# if r == -1:
#     print ("network error")
# elif r == -2:
#     print ("file error")
# elif r == -3:
#     print ("user error")
# else:
#     print ("it worked")
# r = DoSomethingElse()
# if r == -1:
#     print ("network error")
# elif r == -2:
#     print ("file error")
# elif r == -3:
#     print ("user error")
# else:
#     print ("it worked")

