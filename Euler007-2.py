import time

#@profile
def func():
    start = time.time()
#    @profile    
    def isPrime(primes, x):
        sqrtx = int(x**0.5)+1
        for i in primes:
            if x%i==0:
                return False
            elif i>sqrtx:
                return True
        return True
#    @profile
    def it(m):
        yield 2
        array = [2]
        x = 3
        i = 1
        while i <= m:
            if isPrime(array, x):
                array.append(x)
                yield x
                i+=1
            x += 2
    k = 10001
    array = [j for j in it(k)]
    print array[k-1]
    end = time.time()
    print end-start

func()