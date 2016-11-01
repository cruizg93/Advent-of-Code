#http://adventofcode.com/2015/day/3 
#First Problem
#Solution: think about initial position x=0 & y=0 in a cartesian plane, and register every step than santa goes.
#if santa has been in that coordinate that mean he is been there already.
puzzle = input()
addresses = list(puzzle)
house = 1
x = 0
y = 0
houses = []
for currentAddress in addresses:
    if currentAddress == '>':
       x = x+1
    elif currentAddress == '<':
        x =x-1
    elif currentAddress == 'v':
        y = y-1
    elif currentAddress == '^':
        y = y+1
    
    position = "'{},{}'".format(x, y)
    if not position in houses:
        houses.append(position)
        house = house + 1
    
print(house)
    
