from Member import Member


filename = "test.csv"

members = []

with open (filename, "r") as file:
    count = 0
    for line in file:
        
        pieces = line.strip().split(",")
        if count == 0:
            # headings -skip the first line
            count = count + 1
            continue
        else:
            member = Member(int(pieces[0].strip()), 
                                pieces[1].strip(), 
                                pieces[2].strip(),
                                pieces[3].strip() == 'true', 
                                int(pieces[4].strip()))
            members.append(member)


for member in members:

    print(f"{ member.name }\t{ "*" * member.score }")




