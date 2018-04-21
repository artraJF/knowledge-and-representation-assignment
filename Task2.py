# private class for statements that accepts two stings and polarity
class Statements:
    def __init__(self):
        self.subcon = ""
        self.supcon = ""
        self.pol = False

    def create(self, inlist):
        self.subcon = inlist[0]
        self.supcon = inlist[2]
        if inlist[1] == "IS-A":
            self.pol = True
        elif inlist[1] == "IS-NOT-A":
            self.pol = False

    def display(self):
        if self.pol:
            print(self.subcon + " IS-A " + self.supcon)
        elif not self.pol:
            print(self.subcon + " IS-NOT-A " + self.supcon)


# public class for inheritance network that stores a list of statements
class InherNet:
    def __init__(self):
        self.network = []

    def add(self, statement):
        temp = Statements()
        temp.create(statement)
        self.network.append(temp)

    def display(self):
        for i in range(len(self.network)):
            self.network[i].display()


inher = InherNet()
user = ""
while user != ["end"]:
    user = raw_input("Enter statement\n").split(" ")
    if user == ["end"]:
        break
    inher.add(user)
query = Statements()
user = raw_input("Enter query").split(" ")
query.create(user)

