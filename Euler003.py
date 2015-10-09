import time
from math import sqrt

def func():
    start = time.time()
    x = 600851475143
    n = 4
        
    def isprime(f):
        a = 4
        squrt = sqrt(f)
        if f%2 == 0:
            a = 4
            return False
        if f%3 == 0:
            a = 4
            return False
        while a<=squrt:
            if f%a == 0:
                a = 4
                return False
            a+=1
        a = 4
        return True
    
    while n<=x+1/2:
        if n%2 == 0:
            n += 1
        elif n%3 == 0:
            n += 1
        elif x%n == 0 and isprime(n):
            x = x/n
            print n
            n += 1
        else:
            n += 1
    end = time.time()
    print end-start
    
func()