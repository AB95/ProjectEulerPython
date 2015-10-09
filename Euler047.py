import time
import pyximport; pyximport.install(reload_support = True)
import cpriimes

#@profile
def Euler47_2(n):
    primes = cpriimes.func(10**(n-1))
    numDiv = 0
    x = 0
    divs = 0
    while numDiv<n:
        divs = 0
        for i in primes:
            if x%i == 0:
                divs += 1
        if divs == n:
            numDiv += 1
        else:
            numDiv = 0
        x += 1
    print x-n

start = time.time()
Euler47_2(4)
print time.time() - start