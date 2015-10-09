def euler001(n):
    sum = 0
    for i in xrange(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

