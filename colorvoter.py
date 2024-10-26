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

colors = ["R","O","Y","G","B","I","V","K"]
voters = ["Dan","Teresa","Camilla","Ian","Marc","Jonas","Nathan","Neutch"]
rankings = {}

for voter in voters:
    thisranking = colors
    random.shuffle(thisranking)
    rankings[voter]=thisranking
    # print("Added ranking: ", thisranking, " for voter ", voter)
# print(rankings)


def produceallorderings(incolors, depth):
    outorderings = []
    spacer = "> "*depth
    print(spacer, "Produce:",incolors)
    # length = len(remainingcolors)
    # print(length)
    # index = random.randint(0,length-1)
    # print (index)


    all = []
    if len(incolors) == 1:
        print (spacer, "Return:", incolors)
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
            print (spacer, "Recurse:", color,"|",onefewercolors)
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
        print (spacer, "Return:", outorderings)
        return outorderings

# allorderings=produceallorderings(colors)
test = produceallorderings(["A", "B","C","D"], 0)
print("test: ",test)
bestscore=0
bestorderings=[]

# for thisordering in allorderings:
#     thisscore = computescore(thisordering)
#     if thisscore > bestscore:
#         bestorderings=[]
#         bestorderings+=this
#         bestscore=thisscore
# 
# 
# print("Best score: ", bestscore)
# print("Orderings:")
# # print(computemargin(length(bestorderings))+header)
# for index in len(bestorderings):
#     print(index, ". ", bestorderings[index])
