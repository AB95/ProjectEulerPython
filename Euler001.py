def euler1(n):
    total = 0
    for i in xrange(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
