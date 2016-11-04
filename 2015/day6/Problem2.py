# cook your dish here
#http://adventofcode.com/2015/day/6
#If you will try this in local compiler you better try to read the input from a file
# just replace the line numer 14 with the follow code
#
#with open('text.txt') as fin:
# for line in fin:

import sys
import numpy

brightnessCont=0
matriz = numpy.zeros(shape=(1000,1000))
for line in sys.stdin.readlines():
    line = line.split(" ")
    begin = ""
    end = ""
    #1=toggle 2=off 3=on
    action = 0
    
    if line[0] == "toggle":
        begin = line[1].split(",")
        end = line[3].split(",")
        action = 1 
    elif line[1] == "off":
        begin = line[2].split(",")
        end = line[4].split(",")
        action = 2
    elif line[1] == "on":
        begin = line[2].split(",")
        end = line[4].split(",")
        action = 3
    for x in range(int(begin[0]),int(end[0])+1):
        for y in range(int(begin[1]),int(end[1])+1):
            
            if action == 1:
                    matriz[x][y]+=2.2
                    brightnessCont+=2
                    
            elif action ==2:
                if not matriz[x][y] == 0.0:
                    matriz[x][y] -= 1.1
                    brightnessCont-=1
                    
            elif action == 3:
                    brightnessCont+=1
                    matriz[x][y]+=1.1
print(brightnessCont)            
