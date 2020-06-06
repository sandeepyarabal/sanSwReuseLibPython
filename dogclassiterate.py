
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
d.add_trick('bark')
e = Dog('Buddy')   
d.add_trick('barrkbark')
print(d.name)

dogContainer =[]
dogContainer.append(d)
dogContainer.append(e)

for i in dogContainer:
    print(i.name)

def testfun():
    print("testfun")

if __name__=="__main__":
    testfun()