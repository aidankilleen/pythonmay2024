class Record:
    def __init__(self, line):

        pieces = line.strip().split(",")

        self.id = int(pieces[0].strip())
        self.name = pieces[1].strip()
        self.product = pieces[2].strip()
        self.colour = pieces[3].strip()
        self.quantity = int(pieces[4].strip())

    def __str__(self):
        return f"{self.id} {self.name} {self.product} {self.colour} {self.quantity}"


#__name__ is set to __main__ if the module is being run directly
# it is set to the name of the file (without .py extension) if
# the module is being imported
if __name__ == "__main__":
    # test code
    r = Record("1, Fred, card, red, 23")
    print (r)
    
else:
    # do nothing
    pass 