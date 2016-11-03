#http://adventofcode.com/2015/day/4
import hashlib
word = input()

for num in range(1000000):
    digest = hashlib.md5((word + str(num)).encode())
    result = digest.hexdigest()
    if result[:5]=='00000':
        print(word + str(num))
        print(result)
        break
    
