import time

start = time.time()
print str(sum(i**i for i in xrange(1, 1001)))[-10:]
print time.time() - start