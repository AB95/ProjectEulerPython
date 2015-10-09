from time import time

def func(limit):
    phi = [i for i in xrange(limit+1)]

    for i in xrange(2, limit):
        if phi[i] == i:
            phi[i] -= 1
            for j in xrange(i+i,len(phi),i):
                phi[j] = phi[j]/i*(i-1)

    return sum(phi)-1

start = time()
print func(1000000)
print time() - start