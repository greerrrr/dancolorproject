# a program for doing danscolorproject
#
# task: for a set of voters with ranked preferences across a set of colors, produce a good assignment of colors to voters
#
# value: preference maximin:
# - for a given color assignment, each voter has a happiness score from 1-7
#   - first pick: happiness = 7
#   - last pick: happines = 1
# - assignment.score = min(playerhappiness)
# - return max(assignment.score)
import random

# colors = ["R","O","Y","G","B","I","V","K"]
# voters = ["Dan","Teresa","Camilla","Ian","Marc","Jonas","Nathan","Neutch"]
colors = ["Red","Green","Blue","White","Black"]
voters = ["Vera", "Merl", "Tuco","Canopy","Ekhasael"]
votes = {}

for voter in voters:
    #generate a random color sequence,
    #create a vote dictionary
    #where each color stores a score based on their sequence position
    #scores from 0 to length of list
    #descending from the first item down
    random_color_sequence = list(colors)
    random.shuffle(random_color_sequence)
    vote = {}
    for index in range(len(random_color_sequence)):
        color = random_color_sequence[index]
        vote[color] = len(random_color_sequence) - index
    votes[voter]=vote

print("###VOTES###")
print(votes)


def produceallorderings(incolors, depth):
    outorderings = []
    spacer = "> "*depth
    # print(spacer, "Produce:",incolors)
    # length = len(remainingcolors)
    # print(length)
    # index = random.randint(0,length-1)
    # print (index)


    all = []
    if len(incolors) == 1:
        # print (spacer, "Return:", incolors)
        return [incolors]
    else:
        for color in incolors:
            # print (spacer, "outorderings@loop start:",outorderings)
            onefewercolors = list(incolors)
            # print(spacer,"incolors",incolors)
            # print (spacer, "removing ", color)
            # print (spacer, "from ", onefewercolors)
            # print (spacer, "outorderings@before remove:",outorderings)
            onefewercolors.remove(color)
            # print(spacer,"onefewercolors",onefewercolors)
            # print (spacer, "outorderings@before recursion:",outorderings)
            # print (spacer, "Recurse:", color,"|",onefewercolors)
            thisbranch = produceallorderings(onefewercolors, depth+1)
            # print (spacer, "received ",thisbranch)
            # print (spacer, "outorderings@after recursion:",outorderings)
            for ordering in thisbranch:
                # print (ordering, "prepending",color, "before",ordering)
                ordering.insert(0,color)
                # print (spacer, "ordering now ", ordering)
            # print(spacer,"Extend",outorderings,"with",thisbranch)
            outorderings.extend(thisbranch)
            # print (spacer, "outorderings@loop end:",outorderings)
        # print (spacer, "Return:", outorderings)
        return outorderings

# def allunique(suspiciousorderings):
#     for order in suspiciousorderings:
#         testerset.add(order)
#     if len(testerset == len(suspiciousorderings)):
#         return TRUE
#     else:
#         return FALSE


def computevoterscore(voter, assignment):
    color = assignment[voter]
    score = votes[voter][color]
    return score

def computemaximinscore(assignment):
    scores = []
    for voter in voters:
        thisscore = computevoterscore(voter, assignment)
        scores.append(thisscore)
    minscore = min(scores)
    # print(minscore, "lowest of",scores)
    return minscore

def computescore(assignment):
    return computemaximinscore(assignment)

def convert_ordering_to_assignment(ordering):
    assignment = {}
    for index in range(len(voters)):
        assignment[voters[index]] = ordering[index]
    return assignment



print("###ORDERINGS###")
all_orderings=produceallorderings(colors, 0)
print("Qty:",len(all_orderings))
# print("All unique?", allunique(allorderings))
# test = produceallorderings(["A", "B","C","D"], 0)
# print("test: ",test)
# print(all_orderings[1])
# print(convert_ordering_to_assignment(all_orderings[1]))
# convert orderings to assignments
all_assignments = []
for ordering in all_orderings:
    all_assignments.append(convert_ordering_to_assignment(ordering))

best_score=0
best_assignments=[]

for this_assignment in all_assignments:
    this_score = computescore(this_assignment)
    if this_score > best_score:
        best_assignments=[]
        best_assignments.append(this_assignment)
        best_score=this_score


print("Best score: ", best_score,"/",len(colors))
print("Assignments:")
# print(computemargin(length(bestorderings))+header)
for assignment in best_assignments:
    print(assignment)
