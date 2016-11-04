# cook your dish here
#http://adventofcode.com/2015/day/8

import sys
import re
literalStringCont =0
inMemoryCont = 0
for line in sys.stdin.readlines():
    #delete line jump from plain string
    line = line.replace("\n","")
    literalStringCont += len(line)
    
    #starting to proccess the string
    line = re.sub('\A"(.*)"\Z', r'\1', line) # remove quotes
    line = re.sub(r'\\x[0-9A-Fa-f]{2}', 'H', line) # remove hex
    line = re.sub(r'\\"', '"', line) # remove quote
    line = re.sub(r'\\\\', r'\\', line) # remove slash
    inMemoryCont += len(line)
    
print(literalStringCont)
print(inMemoryCont)
print(literalStringCont - inMemoryCont)
