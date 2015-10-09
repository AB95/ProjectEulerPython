##import time
##
#def func():
#    start = time.time()
#    x = 0
#    y = 0
#    
#    for n in xrange (1, 10000001):
#        x += n**2
#        y += n
#    y = y**2
#    print "y = ", y
#    print "x = ", x
#    print y - x
#    end = time.time()
#    print
#    print end-start
#func()

import time
from multiprocessing import Pool
#def func():
start = time.time()
k = 10000001
#x = sum(i**2 for i in xrange(k))
def func(x):
    return x**2
pool = Pool(processes = 4)
x = sum(pool.map(func, xrange(k)))
pool.close()
pool.join()
y = sum(i for i in xrange(k))
yy = y**2
print "x=",x
print "y=",yy
print yy-x
end = time.time()
print
print end-start
    
#func()