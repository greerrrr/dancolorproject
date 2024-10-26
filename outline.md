a program for doing danscolorproject

task: for a set of voters with ranked preferences across a set of colors, produce a good assignment of colors to voters

value: preference maximin:
- for a given color assignment, each voter has a happiness score from 1-7
  - first pick: happiness = 7
  - last pick: happines = 1
- assignment.score = min(playerhappiness)
- return max(assignment.score)

todo:
- convert pseudocode to python
- perhaps, find a way to directly construct an ideal list, or move iteratively through assignment space?
- does *weighting* preferences matter?
- what are the colors?

colors = [ROYGBIVx]
voters = [DTCIMJNN]
ranking = shuffling of ROYGBIV
assignment = shuffling of ROYGBIV (where in assignment[n] is assigned to voters[n]

for each voter {
  input color ranking
  for now, just shuffle colors
  }

allorderings=produceallorderings(colors)

produceallorderings(colors){
  this part is a little squiggly make sure you have the right amount of wrapping
  all = []
  for each color in colors {
    for assignment in produceallorderings(colors.remove(color){
      all += [color]+stublist
  }
  return all

bestscore=0
bestorderings=[]
for thisordering in allorderings {
  thisscore = computescore(thisordering)
  if thisscore > bestscore{
    bestorderings=[]
    bestorderings+=this
    bestscore=thisscore
  }

print "Best score: "+bestscore
print "Orderings:"
print computemargin(length(bestorderings))+header
for index in length(bestorderings){
  print appropriatepadding(index)+bestorderings[index]
