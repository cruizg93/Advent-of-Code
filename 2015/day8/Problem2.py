# cook your dish here
#http://adventofcode.com/2015/day/8
#You must add a \ before every " and \ you encounter. and also wrap the word with " "


import sys
import re
literalStringCont =0
codedStringCont = 0
for line in sys.stdin.readlines():
    #delete line jump from plain string
    line = line.replace("\n","")
    literalStringCont += len(line)
    
    #starting to proccess the string
    line = line.replace('\\','\\\\')
    line = line.replace('"','\\"')
    line = '"'+line+'"'
    codedStringCont += len(line)
    
print(codedStringCont - literalStringCont)
