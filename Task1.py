# Create a class for knowledge base
class KnowledgeBase:
    def __init__(self):
        self.clauses = []

    # Add array of literals (a clause) to array of clauses
    def add(self,literals):
        self.clauses.append(literals)

    # Display clauses in knowledge base separately (for testing)
    def dis(self):
        for i in self.clauses:
            print(i)


def backchain(KnBs, q):
    # Once query is empty then the query is true
    if len(q) == 0:
        return True
    else:
        check = False
        # Switches negated query into positive query to search and vice versa
        if "!" in q[0]:
            q[0] = q[0].replace("!", "")
        else:
            q[0] = "!" + q[0]
        # Searches the KB for q, if found then the new query is the found clause without the result
        # If not found then the function returns false
        for i in KnBs.clauses:
            if q[0] in i:
                # Prints the opposite of the query and in which clause it is found
                print("Found %s in %s" % (q, i))
                i.remove(q[0])
                q = i
                check = True
                break
        if not check:
            return False
        elif check:
            # If the clause found has more than one literal, queries each literal to see if all are true
            # If all are true, returns true, else returns false
            check = True
            for i in range(len(q)):
                if not backchain(KnBs, [q[i]]):
                    check = False
            if not check:
                return False
            elif check:
                return True


KB = KnowledgeBase()
user = ""
# Loop that adds clauses to the knowledge base
while user != ["end"]:
    user = raw_input("Enter clauses in knowledge base (type end to exit)\n").split(", ")
    if user == ["end"]:
        break
    KB.add(user)
# Variable tat stores user input
query = [raw_input("Enter your negated (!) query\n")]
# Temporary storage for output
temp = query[0]
res = backchain(KB, query)
if res:
    print("SOLVED \nKB |= %s" % temp)
elif not res:
    print("NOT SOLVED \nKB does not |= %s" % temp)


'''
# Testing worked
KB = KnowledgeBase()
KB.add(['FirstGrade'])
KB.add(['!FirstGrade', 'Child'])
KB.add(['!Child', '!Male', 'Boy'])
KB.add(['!Kindergarten', 'Child'])
KB.add(['!Child', '!Female', 'Girl'])
KB.add(['Female'])
KB.add(['Male'])
query = ['!Boy']
store = query[0]
test = backchain(KB, query)
if test:
    print("SOLVED \nKB |= %s" % store)
elif not test:
    print("NOT SOLVED \nKB does not |= %s" % store)
'''
