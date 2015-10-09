import pyximport; pyximport.install()
import cpriimes

primes = cpriimes.func(2000000)

def isPrime(i):
    if cpriimes.isPrime(i, primes):
        return True
    return False

def isTruncPrime(i):
    string = str(i)
    for i in xrange(len(string)):
        if isPrime(int(string[i:])) == 0:
            return False
        elif isPrime(int(string[:i+1])) == 0:
            return False
    return True
    
array = []
i = 10
while len(array)<11:
    if isTruncPrime(i): 
        array.append(i)
    i += 1
print sum(array)