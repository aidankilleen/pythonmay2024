from Member import Member

filename = "test.csv"
members = []

with open (filename, "r") as file:
    count = 0
    for line in file:
        
        pieces = line.strip().split(",")
        if count == 0 or len(pieces) != 5:
            # headings or invalid line - skip
            # note - skipping invalid lines might not be a good idea for data imports
            count = count + 1
            continue
        else:
            try:
                id = int(pieces[0].strip())
            except:
                id = 0
            
            name = pieces[1].strip()
            email = pieces[2].strip()
            active = pieces[3].strip() == 'true'
           
            try:
                score = int(pieces[4].strip())
            except:
                score = 0
                
            member = Member(id, 
                                name, 
                                email,
                                active, 
                                score)
            
            members.append(member)
for member in members:
    print(f"{ member.name }\t{ "*" * member.score }")
