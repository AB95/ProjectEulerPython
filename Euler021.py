import time

def d(n):
    return sum(i for i in xrange(1, n) if n%i == 0)
    
def func(top):
    return sum(i for i in xrange(1, top) if i == d(d(i)) and i != d(i))
    
start = time.time()
print func(10000)
print time.time() - start