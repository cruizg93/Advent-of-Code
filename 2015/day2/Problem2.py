#DOES NOT WORK!!!!
#http://adventofcode.com/2015/day/2
#Grab the two smallest sides multiple each by 2 and added together
#then multiple every side with each other and the total added to the other operation result
import sys
totalPaper = 0
for line in sys.stdin.readlines():
    dimensions = line.replace('\n', '').split('x')
    dimensions = list(map(int,dimensions))
    dimensions.sort()
    wrap = (dimensions[0]*2)+(dimensions[1]*2)
    ribbon = dimensions[0]*dimensions[1]*dimensions[2]
    totalPaper+=wrap+ribbon
print(totalPaper)
    
