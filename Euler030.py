import time

def func(i, n):
    tot = 0
    for j in str(i):
        tot += int(j)**n
    if tot != i: return False
    else: return True

start = time.time()
print sum(i for i in xrange(2, 1000000) if func(i, 5))
print time.time() - start