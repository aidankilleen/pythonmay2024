

list = ["red", "green", "blue", "red", "orange", "blue", "red", "green", "purple", "red", "orange"]

# goal - get a distinct list of the colours

# manual approach
distinct_list = []
for colour in list:
    if colour not in distinct_list:
        distinct_list.append(colour)

print (distinct_list)
# data structure called a set
unique_list = set(list)
print (unique_list)

unique_list.add("pink")
print (unique_list)

# adding an item that already exists doesn't change the list
unique_list.add("red")
print (unique_list)

# data structures
# list / arrays []
# tuple () - immutable or read-only array
# dictionary [] - unordered list of key value pairs
# set {} - distinct list of unique items
# objects - user-defined data structures













