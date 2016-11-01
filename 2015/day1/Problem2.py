#http://adventofcode.com/2015/day/1
#Second Problem
puzzle = input()
floors = list(puzzle)
currentFlorr = 0
indexCount = 0
for nextFloor in floors:
    if nextFloor == '(':
        currentFlorr += 1
    elif nextFloor == ')':
        currentFlorr -=1
    indexCount += 1
    if currentFlorr == -1:
        break
print(indexCount)
