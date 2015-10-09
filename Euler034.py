from math import factorial
import time

def func(i):
    if sum(factorial(int(j)) for j in str(i))==i: return True
    return False

start = time.time()
x = raw_input("number: ")
print x
print sum(i for i in xrange(3, int(x)) if func(i))
print time.time() - start

