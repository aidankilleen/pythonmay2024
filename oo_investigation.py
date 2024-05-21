print ("oo investigation")

class Member:
    #__init__ method is called when the object is instantiated
    def __init__(self, id, name, email, active, score):
        # properties of the object are set in the __init__ method
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        self.score = score

    def __str__(self):
        return f"{self.id} {self.name} {self.email} {self.score} {"Active" if self.active else "Inactive"}"
    
    def display(self):
        print (member.id)
        print (member.name)
        print (member.email)
        print ("Active" if member.active else "Inactive")
        print (f"Score: {"*" * member.score}")

member = Member(1, "Alice","alice@gmail.com", True, 10)

member.display()

members = [
    Member(1, "Alice","alice@gmail.com", True, 10), 
    Member(2, "Bob","bob@gmail.com", False, 10), 
    Member(3, "Carol","carol@gmail.com", False, 10), 
    Member(4, "Dan","dan@gmail.com", True, 10), 
]

for member in [m for m in members if not m.active]:
    print(member)
