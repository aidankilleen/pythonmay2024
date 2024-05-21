
filename = "test.csv"

members = []

with open(filename, "r") as file:
    count = 0
    for line in file:
        
        pieces = line.strip().split(",")
        if count == 0:
            # headings -skip the first line
            count = count + 1
            continue
        else:
            member = {
                'id': int(pieces[0].strip()), 
                'name': pieces[1].strip(), 
                'email': pieces[2].strip(), 
                'active': pieces[3].strip() == 'true', 
                'score': int(pieces[4].strip())
            }
            members.append(member)
        count = count + 1

print ("*" * 25)
active_members = [m for m in members if m['active']]
print (active_members)
print ("*" * 25)
inactive_members = [m for m in members if not m['active']]
print (inactive_members)

for member in members:
    print (f"{member['name']}:\t { '*' * member['score']}")