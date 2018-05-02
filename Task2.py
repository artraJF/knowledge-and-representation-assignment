# private class for statements that accepts two stings and polarity
class Statement:
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

    # For testing
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
        temp = Statement()
        temp.create(statement)
        self.network.append(temp)

    # For testing
    def display(self):
        for i in range(len(self.network)):
            self.network[i].display()

    # Method that stores in a jumbled fashion, every correct path in an array
    def _buildpaths(self, q, goal, store):
        if q == goal:
            return
        else:
            for i in self.network:
                if i.subcon == q:
                    store.append(i)
                    self._buildpaths(i.supcon, goal, store)

    # Method that separates paths into different arrays (2d)
    def _splitpaths(self, arr, goal):
        temp2 = []
        x = 0
        for i in range(len(arr)):
            temp = []
            if arr[i].supcon == goal:
                for j in range(x, i+1):
                    temp.append(arr[j])
                x = i+1
                temp2.append(temp)
        return temp2

    # Method that polishes paths, builds them entirely
    def _polpaths(self, arr):
        for i in range(1, len(arr)):
            j = 0
            temp = []
            if arr[0][0].subcon != arr[i][0]:
                while arr[0][j].subcon != arr[i][0].subcon:
                    temp.append(arr[0][j])
                    j = j+1
                for x in range(len(arr[i])):
                    temp.append(arr[i][x])
            arr[i] = temp

    # Removes redundant paths
    def _redunpaths(self, arr, goal):
        tmparr = []
        for i in range(len(arr)):
            check = True
            for j in range(len(arr[i])):
                if arr[i][j].pol == False and arr[i][j].supcon != goal:
                    check = False
            if not check:
                tmparr.append(arr[i])
        for i in range(len(tmparr)):
            arr.remove(tmparr[i])

    # Method that displays all paths neatly
    def _dispaths(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j == 0:
                    print(arr[i][j].subcon),
                if arr[i][j].pol:
                    print("IS-A"),
                elif not arr[i][j].pol:
                    print("IS-NOT-A"),
                if arr[i][j].supcon == "Gray":
                    print(arr[i][j].supcon)
                else:
                    print(arr[i][j].supcon),

    # Method that determines shortest path
    def _shortpath(self, arr):
        tmparr = arr[0]
        for i in range(1,len(arr)):
            if len(arr[i]) < len(tmparr):
                tmparr = arr[i]
        return tmparr

    # Method that simplifies input
    def buildpaths(self, q):
        temparr = []
        self._buildpaths(q.subcon, q.supcon, temparr)
        temparr = self._splitpaths(temparr, q.supcon)
        self._polpaths(temparr)
        self._redunpaths(temparr, q.supcon)
        print("All paths: \n")
        self._dispaths(temparr)
        print("\nShortest path: \n")
        self._dispaths([self._shortpath(temparr)])


'''
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
'''

inher = InherNet()
inher.add(["Clyde", "IS-A", "FatRoyalElephant"])
inher.add(["FatRoyalElephant", "IS-A", "RoyalElephant"])
inher.add(["Clyde", "IS-A", "Elephant"])
inher.add(["RoyalElephant", "IS-A", "Elephant"])
inher.add(["RoyalElephant", "IS-NOT-A", "Gray"])
inher.add(["Elephant", "IS-A", "Gray"])
query = Statement()
query.create(["Clyde", "IS-A", "Gray"])
inher.buildpaths(query)
