import time

def func():
    results = []
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            results.append (a**b)
    return results

start = time.time()
print len(set(func()))
end = time.time()
print end-start