import time

def func():
    a = 0
    b = 0 
    n = 0
    ans = [0, 0, 0] #a, b, n
    primes = [2, 3, 5, 7]
    
    def isPrime(primes, x):
        if x>1:
            sqrtx = int(x**0.5)+1
            for i in primes:
                if x%i==0:
                    return False
                elif i>sqrtx:
                    if x not in primes:
                        primes.append(x)
                    return True
            return True
            
    for a in xrange(-1000, 1001):
        for b in xrange(-1000, 1001):
            xl = (n**2) + (a*n) + b
            while isPrime(primes, xl):
                n += 1
                xl = (n**2) + (a*n) + b
            if n > ans[2]:
                ans[0] = a
                ans[1] = b
                ans[2] = n
            n = 0
    print primes
    return ans
    
start = time.time()
print func()[0] * func()[1]
end = time.time()
print end - start