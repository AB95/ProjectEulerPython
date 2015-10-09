import time

@profile
def func():
    start = time.time()
    longestc = 0
    largestn = 0
    k = 10000
    for x in xrange(1, k):
        n = x
        c = 1
        while n != 1:
            if n % 2 == 0:
                n = n/2
                c+=1
            else:
                n = 3 * n + 1
                c+=1
        if c>longestc:
            longestc = c
            largestn = x
    
    print longestc        
    print largestn
    
    end = time.time()
    timet = end-start
    print timet
    
func()