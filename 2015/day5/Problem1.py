#http://adventofcode.com/2015/day/5
import sys
vowels = ['a', 'e', 'i', 'o', 'u']
nogoods = ['ab', 'cd', 'pq', 'xy']
niceWordCont = 0
def checkVowels(characterArray):
    for character in characterArray:
        if character in vowels:
            return True
    return False

def checkDoubleChar(characterArray):
    indexCount =0
    for character in characterArray:
        if indexCount < characterArray.lenght():
            

for line in sys.stdin.readlines():
    character = list(line)
    if checkVowels(character) == True and  
    print(checkVowels(character))
