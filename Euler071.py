from time import time

def func(k):
    a, b = 0, 1
    c, d = 1, 1
    p, q, = 0, 0
    while b + d <= k:
        p, q = a+c, b+d
        if p/float(q) >= 3/7.0:
            c, d, = p, q
        else:
            a, b = p, q
    print p, q

start = time()
func(1000000)
print time() - start
