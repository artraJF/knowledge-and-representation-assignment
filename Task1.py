# Create a class for knowledge bade
class KnowledgeBase:
    def __init__(self):
        self.clauses = []

    # Add array of literals (a clause) to array of clauses
    def add(self,literals):
        self.clauses.append(literals)

    # Display clauses in knowledge base separately
    def dis(self):
        for i in self.clauses:
            print(i)


def backchain(KnBs, q):
    # Once query is empty then the query is true
    if len(q) == 0:
        return True
    else:
        check = False
        # Switches negated query into positive query to search
        while "!" in q[0]:
            q[0] = q[0].replace("!", "")
        # Searches the KB for q, if found then the new query is the found clause without the result
        # If not found then the function returns false
        for i in KnBs.clauses:
            if q[0] in i:
                i.remove(q[0])
                q = i
                check = True
                break
        if not check:
            return False
        elif check:
            # If the clause found has more than one literal, queries each literal to see if all are true
            # If all are true, returns true, else returns false
            if len(q) > 1:
                check = True
                for i in range(len(q)):
                    if not backchain(KnBs, q):
                        check = False
                if not check:
                    return False
                elif check:
                    return True
            # If one literal was found, the new query is that literal
            else:
                temp = backchain(KnBs, q)
                if temp:
                    return True
                elif not temp:
                    return False


'''
KB = KnowledgeBase()
user = ""
while user != ["end"]:
    user = raw_input("Enter clauses in knowledge base (type end to exit)\n").split(", ")
    if user == ["end"]:
        break
    KB.add(user)
query = raw_input("Enter your negated (!) query\n")
'''

# First test worked, more testing required
KB = KnowledgeBase()
KB.add(['!fly', '!cheep', 'frog'])
KB.add(['!croak', '!jump', 'bird'])
KB.add(['!green', 'bird'])
KB.add(['!blue', 'frog'])
query = ['!']
test = backchain(KB, query)
if test:
    print("Yay")
elif not test:
    print("Boo")
