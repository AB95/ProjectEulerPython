from itertools import permutations
from math import sqrt

def isPrime(x):
    if x%2 == 0:
        return False
    for i in xrange(3, int(sqrt(x))+1, 2):
        if x%i == 0:
            return False
    return True

permutNums = []
string = "123456789"        
for i in xrange(8,5,-1):
    permutNums.append(string)
    string = string[:i]       
#print permutNums

totNums = []
for ll in permutNums:    
    nums = [i for i in permutations(ll)]
    for i in xrange(len(nums)):
        string = ""
        for j in nums[i]:
            string += j
        nums[i] = int(string)
    nums = list(set(nums))
    totNums.extend(nums)

#print totNums
print max(i for i in totNums if isPrime(i))
#print len([2] + [i for i in nums if isPrime(i)])