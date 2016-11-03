#http://adventofcode.com/2015/day/4
import hashlib
key = input() #my given puzzle key bgvyzdsv

for num in range(1000000):
    digest = hashlib.md5((key + str(num)).encode())
    result = digest.hexdigest()
    if result[:5]=='00000':
        print(key + str(num))
        print(result)
        break
    
