def func(n):
    for b in xrange(1, n):
        for a in xrange(1, b):
            c = n - (a + b)
            if a**2 + b**2 == c**2:
                return a*b*c

print func(1000)
