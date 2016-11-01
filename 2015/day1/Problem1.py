#http://adventofcode.com/2015/day/1
#First Problem
puzzle = input()
floors = list(puzzle)
currentFlorr = 0
for nextFloor in floors:
    if nextFloor == '(':
        currentFlorr += 1
    elif nextFloor == ')':
        currentFlorr -=1
        
print(currentFlorr)
