import pyximport; pyximport.install(reload_support = True)
import cpriimes

primes = cpriimes.func(1000000)
isP = cpriimes.isPrime

def isPrime(i):
    return isP(i, primes)

def isCirclePrime(num):
    for i in xrange(len(str(num))):
        if isPrime(int(str(num)[i:] + str(num)[:i])) == 0:
            return False
    return True
    
print len([i for i in xrange(1000000) if isCirclePrime(i)])