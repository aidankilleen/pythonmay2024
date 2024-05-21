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
        print (self.id)
        print (self.name)
        print (self.email)
        print ("Active" if self.active else "Inactive")
        print (f"Score: {"*" * self.score}")
