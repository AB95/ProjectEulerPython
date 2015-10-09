

#def func(top):
#    def relPrime(x):
#        primes = [1]
#        if x%2 == 0:
#            for i in xrange(3, x, 2):
#                if  x%i != 0:
#                    primes.append(i)
#        else:
#            for i in xrange(2, x):
#                if x%i != 0:
#                    primes.append(i)
#        return (len(primes))
#        
#    maxi = 0
#    maxi2 = 0
#    for i in xrange(top):
#        print relPrime(i)
#        if i/relPrime(i) > maxi2:
#            maxi = i
#            maxi2 = i/relPrime(i)
#    
#    return maxi
#    
#print func(10)
import Euler10

primes = Euler10.func(1000000)

ans = 1
i = 0
while ans*primes[i] < 1000000:
    ans *= primes[i]
    i+=1
    
print ans