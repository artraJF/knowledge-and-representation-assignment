# private class for statements that accepts two stings and polarity
class Statement:
    # Method that initialises statement
    def __init__(self):
        self.subcon = ""
        self.supcon = ""
        self.pol = False

    # Method creates a statement
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
    # Initialises array
    def __init__(self):
        self.network = []

    # Appends statements to the network
    def add(self, statement):
        temp = Statement()
        temp.create(statement)
        self.network.append(temp)

    # For testing
    def display(self):
        for i in range(len(self.network)):
            self.network[i].display()

    # Method that stores in, a jumbled fashion, every correct path in an array.
    def _buildpaths(self, q, goal, store):
        # If the sub-concept is the same as the goal then the recursion stops.
        if q == goal:
            return
        # Else searches the entire network for a matching sub-concept.
        # Once found, appends statement to store, then searches again using the super-concept of the statement found
        # as a query.
        else:
            for i in self.network:
                if i.subcon == q:
                    store.append(i)
                    self._buildpaths(i.supcon, goal, store)

    # Method that separates paths into different arrays (2d)
    def _splitpaths(self, arr, goal):
        # Searches the super-concepts within the array that match the goal.
        # Once found, the array is split until every row within the 2d array has one super-concept = goal.
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

    # Method that adds missing statements to paths
    def _polpaths(self, arr, q):
        # Goes through all paths until a pth that doesn't start with the query's sub-concept is found.
        # Once found, adds the missing statements, taken from the last path that started with the sub-concept, and adds
        # them to a temporary variable. The rest are added from the path with the missing statements and is then
        # replaced with the temporary variable.
        tmpvar = []
        for i in range(len(arr)):
            if arr[i][0].subcon == q:
                tmpvar = arr[i]
            else:
                temp = []
                j = 0
                while tmpvar[j].subcon != arr[i][0].subcon:
                    temp.append(tmpvar[j])
                    j = j+1
                temp = temp + arr[i]
                arr[i] = temp

    # Removes redundant paths
    def _redunpaths(self, arr, goal):
        # Searches the array for polarities that are false.
        # If a false polarity is found and the super-concept is not equal to the goal, then the entire path is removed.
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
    def _dispaths(self, arr, goal):
        # Goes through entire array. If it is the first element of the path, the sub-concept is the displayed, as well
        # as the polarity and super-concept. Else, only the polarity and super-concept are displayed.
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j == 0:
                    print(arr[i][j].subcon),
                if arr[i][j].pol:
                    print("IS-A"),
                elif not arr[i][j].pol:
                    print("IS-NOT-A"),
                if arr[i][j].supcon == goal:
                    print(arr[i][j].supcon)
                else:
                    print(arr[i][j].supcon),

    # Method that determines shortest path
    def _shortpath(self, arr):
        # Goes through array of paths matching their sizes until the smallest length is found.
        tmparr = arr[0]
        retarr = []
        for i in range(1,len(arr)):
            if len(arr[i]) < len(tmparr):
                tmparr = arr[i]
        retarr.append(tmparr)
        for i in range(len(arr)):
            if len(arr[i]) == len(tmparr) and arr[i] != tmparr:
                retarr.append(arr[i])
        return retarr

    # Method that determines the inferential path
    def _inferpath(self, arr):
        # First, the method searches for the longest path (the most detailed).
        tmparr = arr[0]
        for i in range(1,len(arr)):
            if len((arr[i])) > len(tmparr):
                tmparr = arr[i]
        tmpvar = tmparr[len(tmparr)-1]
        retarr = []
        # Once the longest path is found, the method grabs the last statement, and matches the polarity with the last
        # statement of other paths. If a contradiction is found, then the path is appended to a return array.
        # If no contradictions are found, then the method takes the longest path as the inferential path.
        for i in range(len(arr)):
            tmpvar2 = arr[i][len(arr[i])-1]
            if tmpvar.pol != tmpvar2.pol:
                retarr.append(arr[i])
        if len(retarr) == 0:
            retarr.append(tmparr)
            return retarr
        else:
            return retarr

    # Method that uses all previous private methods (starting with an '_') to simplify input.
    def buildpaths(self, q):
        temparr = []
        self._buildpaths(q.subcon, q.supcon, temparr)
        temparr = self._splitpaths(temparr, q.supcon)
        self._polpaths(temparr, q.subcon)
        self._redunpaths(temparr, q.supcon)
        print("\nAll paths: \n")
        self._dispaths(temparr, q.supcon)
        print("\nShortest paths: \n")
        self._dispaths(self._shortpath(temparr), q.supcon)
        print("\nInferential paths: \n")
        self._dispaths(self._inferpath(temparr), q.supcon)


# Main method for user input
IN = InherNet()
user = ""
print("Type end to close the inheritance network. Use space to separate every concept and use IS-A and IS-NOT-A (case "
      "sensitive)\nInput example: Penguin IS-A Bird")
while user != ["end"]:
    user = raw_input("Enter statement\n").split(" ")
    if user == ["end"]:
        break
    IN.add(user)
query = Statement()
user = raw_input("Enter query\n").split(" ")
query.create(user)
IN.buildpaths(query)

# Static values for testing
'''
IN = InherNet()
IN.add(["Clyde", "IS-A", "FatRoyalElephant"])
IN.add(["FatRoyalElephant", "IS-A", "RoyalElephant"])
IN.add(["Clyde", "IS-A", "Elephant"])
IN.add(["RoyalElephant", "IS-A", "Elephant"])
IN.add(["RoyalElephant", "IS-NOT-A", "Gray"])
IN.add(["Elephant", "IS-A", "Gray"])
query = Statement()
query.create(["Clyde", "IS-A", "Gray"])
IN.buildpaths(query)
'''