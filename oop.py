import os

os.system("clear")

class Bird:
    # class attribute
    numBirds = 0
    
    # constructor - functions that runs everytime we create a new bird
    def __init__(self, kind, call):   # self keyword to refer to an instance of bird
        # instance variable/properties
        self.kind = kind
        self.call = call   # created 2 instances that will belong to the Bird class
        Bird.numBirds += 1    #increases the number of birds
        print(f"Number of birds = {Bird.numBirds}")

    # behaviour / method
    def describe(self):    #describes which bird it is and sound it makes
        return f"{self.kind} goes {self.call}."


class Big_Bird(Bird):  #created new class based on previous one

    def __init__(self, kind, call, wingspan):   #inherited constructor, adding new instance
        self.wingspan = wingspan
        super().__init__(kind, call)   #call the init instance

    def describe(self):
        return f"{self.kind} goes {self.call}, and has a wingspan of {self.wingspan} feet."


owl = Bird("Owl", "Twit Twoo")  #created an instance of the Bird class, increases the numbers of birds on the class

crow = Bird("Crow", "Caw")

print(owl.describe())

print(owl.call)

eagle = Big_Bird("Eagle", "Screech", 25)

print(eagle.wingspan)
print(eagle.describe())