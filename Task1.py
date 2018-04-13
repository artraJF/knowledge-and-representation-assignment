# Object of type clause
class clause():
    def __init__(self):
        self.literals = []

    def add(self, literal):
        self.literals.append(literal)


user, arr = [], []
while user != ["end"]:
    test = clause()
    user = raw_input("Enter literals\n").split(", ")
    if user != ["end"]:
        test.add(user)
        arr.append(test)

for i in range(len(arr)):
    print(arr[i].literals)


