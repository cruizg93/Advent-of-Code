#http://adventofcode.com/2015/day/2

import sys
total = 0
for line in sys.stdin.readlines():
    dimensions = line.replace('\n', '').split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    extra = 0
    
    side1 = l*w
    side2 = l*h
    side3 = w*h
    area = 2*side1 + 2*side2 + 2*side3
    
    if side1 < side2 and side1 < side3:
        extra = side1
    elif side2< side3 and side2 < side1:
        extra = side2
    elif side3 < side1 and side3 < side2:
        extra = side3
    total += extra+area

print(total)
    
