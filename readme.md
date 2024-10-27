a program for doing danscolorproject

task: for a set of voters with ranked preferences across a set of colors, produce a good assignment of colors to voters

value: preference maximin:
- for a given color assignment, each voter has a happiness score from 1-7
  - first pick: happiness = 7
  - last pick: happines = 1
- assignment.score = min(playerhappiness)
- return max(assignment.score)

todo:
- verify uniqueness of each ordering
- tidy code, generally
- use nicer debugging system
- perhaps, find a way to directly construct an ideal list, or move iteratively through assignment space?
- does *weighting* preferences matter?
- what are the colors?
