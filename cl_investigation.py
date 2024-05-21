import sys

print ("CL Investigation (Command Line parameters)")
print (f"Script: {sys.argv[0]}")
print (f"Parameters: {sys.argv[1:]}")

if len(sys.argv) < 2:
    print ("Usage:")
    print (f"{sys.argv[0]} FILE")
    exit()

filename = sys.argv[1]

with open(filename, "r") as file:
    count = 0
    for line in file:
        count +=1

print (f"there are { count } lines in {filename}")

print (sys.platform)
print (sys.flags)



