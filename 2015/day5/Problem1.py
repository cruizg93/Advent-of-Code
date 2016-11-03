#http://adventofcode.com/2015/day/5
import sys
vowels = ['a', 'e', 'i', 'o', 'u']
nogoods = ['ab', 'cd', 'pq', 'xy']
niceWordCont = 0
howManyNice = 0
def checkVowels(characterArray):
    vowelCont = 0
    for character in characterArray:
        if character in vowels:
            vowelCont += 1
        if vowelCont == 3:
            return True
    return False

def checkDoubleChar(characterArray):
    indexCount =1
    for character in characterArray:
        if indexCount < len(characterArray):
            if character == characterArray[indexCount]:
                return True
        indexCount += 1        
    return False
            
def haskNoGoods(line):
    for bad in nogoods:
        if bad in line:
            return True
    return False  
    
for line in sys.stdin.readlines():
    character = list(line)
    haskNoGoods(character)
    if checkVowels(character) and checkDoubleChar(character):
        if not haskNoGoods(line):
            howManyNice += 1
    
print(howManyNice)
