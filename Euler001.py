import time


#@profile
# def func():
#     return sum(n for n in xrange(1000) if n%3 == 0 or n%5 == 0)
#
# start = time.time()
# print func()
# end = time.time()
# print end-start

def func():
    start = time.time()
    sum = 0
    for i in xrange(100000000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return time.time() - start

print func()