# Create a class for knowledge base
class KnowledgeBase:
    # Initialises knowledge base
    def __init__(self):
        self.clauses = []

    # Add array of literals (a clause) to array of clauses
    def add(self,literals):
        self.clauses.append(literals)

    # Display clauses in knowledge base separately (for testing)
    def dis(self):
        for i in self.clauses:
            print(i)

    # Using same algorithm as before to accept more than 1 literal
    def backchain(self, q):
        # If query is empty then query entails knowledge base
        if len(q) == 0:
            return True
        else:
            check = False       # Variable used later to check whether a matching literal is found
            # If query only contains 1 literal, its polarity is changed, then searches the KB to find a matching literal
            # If a literal is found check is set to true,
            # and the new query is the clause found minus the matching literal
            # Later, if check is true the query continues on, else the current method returns false
            if len(q) == 1:
                if "!" in q[0]:
                    q[0] = q[0].replace("!", "")
                else:
                    q[0] = "!" + q[0]
                for i in KB.clauses:
                    if q[0] in i:
                        print("Found %s in %s" % (q, i))
                        i.remove(q[0])
                        q = i
                        check = True
                        break
                if not check:
                    return False
                elif check:
                    if self.backchain(q):
                        return True
                    elif not self.backchain(q):
                        return False
            # If query has multiple literals then the method checks whether all literals are in the knowledge base,
            # splits clause into singular literals a recursively calls the method again
            else:
                check = True
                for i in range(len(q)):
                    if not self.backchain([q[i]]):
                        check = False
                        break
                if check:
                    return True
                elif not check:
                    return False


# Main method that allows user input
KB = KnowledgeBase()
user = ""
print("Enter clauses line by line. Use ! for negation and type end (case sensitive) to close the knowledge base.")
print("Make sure that literals are separated with a , \nExample: !Mammal, Human")
# Loop that adds clauses to the knowledge base
while user != ["end"]:
    user = raw_input("Enter a clause in knowledge base\n").split(", ")
    if user == ["end"]:
        break
    KB.add(user)
# Variable that stores user input
query = [raw_input("Enter your negated (!) query\n")]
# Temporary storage for output
temp = query
res = KB.backchain(query)
if res:
    print("SOLVED \nKB |= %s" % temp)
elif not res:
    print("NOT SOLVED \nKB does not |= %s" % temp)

# Static input for testing
'''
KB = KnowledgeBase()
KB.add(['FirstGrade'])
KB.add(['!FirstGrade', 'Child'])
KB.add(['!Child', '!Male', 'Boy'])
KB.add(['!Kindergarten', 'Child'])
KB.add(['!Child', '!Female', 'Girl'])
KB.add(['Female'])
KB.add(['Male'])
query = ['!Boy', '!Girl']
store = query
test = KB.backchain(query)
if test:
    print("SOLVED \nKB |= %s" % store)
elif not test:
    print("NOT SOLVED \nKB does not |= %s" % store)
'''