#@profile

import time
def func():
    
    start = time.time()
    x = 1
    y = 1
    total = 0
    k = 4000000
    while x<=k or y<=k:
        if x%2 and x<=k:
            total += x
        if y%2 and y<=k:
            total += y
        x += y
        y += x
    print total
    end = time.time()
    timet = end - start
    print timet
    
func()