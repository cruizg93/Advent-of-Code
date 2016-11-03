#http://adventofcode.com/2015/day/4
import hashlib
key = input() #my given puzzle key bgvyzdsv

for num in range(1000000000):
    digest = hashlib.md5((word + str(num)).encode())
    result = digest.hexdigest()
    if result[:6]=='000000':
        print(word + str(num))
        print("/*"+result)
        break
    
