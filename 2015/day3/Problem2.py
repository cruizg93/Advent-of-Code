#http://adventofcode.com/2015/day/3 
#Second Problem
#Solution: just add double position but register both steps on the same cartesian plane

puzzle = input()
addresses = list(puzzle)
house = 1
x = 0
y = 0
robotx = 0
roboty = 0
houses = ['0,0']
indexCont = 1
for currentAddress in addresses:
    if currentAddress == '>':
        if(indexCont % 2 == 0):
           x += 1
        else:
            robotx += 1    
            
    elif currentAddress == '<':
        if(indexCont % 2 == 0):
           x -= 1
        else:
            robotx -= 1
            
    elif currentAddress == 'v':
        if(indexCont % 2 == 0):
           y -= 1
        else:
            roboty -= 1
        
    elif currentAddress == '^':
        if(indexCont % 2 == 0):
           y += 1
        else:
            roboty += 1
    
    if(indexCont % 2 == 0):
        position = '{},{}'.format(x, y)
    else:
        position = '{},{}'.format(robotx, roboty)
    
    
    if not position in houses:
        
        houses.append(position)
        house = house + 1
    indexCont += 1
print(house)
    
