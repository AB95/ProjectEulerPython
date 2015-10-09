import time
from math import sqrt

def func():
    start = time.time()
    max = 2000000
    squrt = int(sqrt(max))
        
    array = [True] * max
    def mark(array, x):
        for i in xrange(x+x, len(array), x):
            array[i] = False
    
    array[0] = False
    array[1] = False
    
    num = 0    
    
    for j in xrange(2, squrt+1):
        mark(array, j)
        if array[j]:
            num += 1
            print num
            if num == 10001:
                print j
    #        print j
    
    for i in xrange(0, len(array)):
        if array[i]:
            num += 1
        if num == 10001:
            print i, "k"
            break
    end = time.time()
    timet = end - start
    print timet
func()