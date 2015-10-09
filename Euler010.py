from math import sqrt
import time


def func(top):
    start = time.time()
    squrt = int(sqrt(top))
    
    array = [True] * top
    def mark(array, x):
        for i in xrange(x*x, len(array), x):
            array[i] = False
    
    array[0] = False
    array[1] = False
    
    for j in xrange(2, squrt+1):
        mark(array, j)
    #        print j
    
    print sum(s for s in xrange(0, len(array)) if array[s])
    # return [s for s in xrange(0, len(array)) if array[s]]
    end = time.time()
    timet = end - start
    print timet

func(2000000)
