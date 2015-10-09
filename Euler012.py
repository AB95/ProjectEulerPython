import time
from math import sqrt

def func():
    start = time.time()
    x = 0
    d = 0
    t = 0
    
    while d < 500:
        x+=1
        d = 0
        t = 0
        t += sum(i for i in xrange(1, x+1))
        squrt = int(sqrt(t))
        for j in xrange(1, squrt+1):
            if t%j == 0:
                d += 2
    print t
    end = time.time()
    print end - start
func()