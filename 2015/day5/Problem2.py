# cook your dish here
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
            line = line.replace(pair,"",1)
            if pair in line[1:]:
                return pair
            
        indexCount +=1
    
    return "0"
    
def checkletterRepeated(line):
    characterArray = list(line)
    secondLetterAhead = 2
    for character in characterArray:
        if secondLetterAhead < len(characterArray):
            if character == characterArray[secondLetterAhead]:
                print(character)
                return True
        secondLetterAhead += 1       
    return False
    
for line in sys.stdin.readlines():
    character = list(line)
    pair = checkDoubleCharTwice(line)
    if  not pair == "0":
        line = line.replace(pair,"",2)
        if checkletterRepeated(line):
            print(pair,line)
            howManyNice += 1
print(howManyNice)
