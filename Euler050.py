from math import sqrt

def func(k):
    
    def isPrime(x):
            sqrtx = sqrt(x)
            for i in primes:
                if x%i == 0:
                    return False
                elif i>sqrtx:
                    return True
                    
    primes = [2, 3, 5]
    
    primes += (i for i in xrange(7, k) if isPrime(i))
    
    leng = len(primes)
    
    maxCount = 0
    for i in xrange(leng):
        tot = sum(primes[i:])
        for j in xrange(leng-1, i, -1):
            tot -= primes[j]
            if tot < k and j - i > maxCount and isPrime(tot):
                maxCount = j-i
                num = tot
    print num
    
func(1000)