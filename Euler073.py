from time import time

def func(n):
    a, b, c, d = 0, 1, 1, n
    count = 0
    while c/float(d) < 0.5:
        if c/float(d) > 1/3.0:
            count += 1
        k = int((n+b)/(float(d)))
        a, b, c, d, = c, d, k*c-a, k*d-b
        print (a, b)
    return count

start = time()
print func(8)
print time() - start
