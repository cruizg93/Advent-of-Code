# cook your dish here
#http://adventofcode.com/2015/day/5
import sys
import re
howManyNice = 0

def checkDoubleCharTwice(line):
    indexCount =1
    characterArray = list(line)
    
    for character in characterArray:
        if indexCount < len(characterArray):
            pair = character+characterArray[indexCount]
            auxline = line
            if pair in line[(indexCount+1):]:
                return True
            
        indexCount +=1
    
    return False
    
def checkletterRepeated(line):
    characterArray = list(line)
    secondLetterAhead = 2
    for character in characterArray:
        if secondLetterAhead < len(characterArray):
            if character == characterArray[secondLetterAhead]:
                return True
        secondLetterAhead += 1       
    return False
    
for line in sys.stdin.readlines():
    character = list(line)
    
    if  checkDoubleCharTwice(line) and checkletterRepeated(line):
            howManyNice += 1
print(howManyNice)
