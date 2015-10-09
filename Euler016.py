for x in xrange(0, 1001,4):
    n = 2**x    
    t = 0
    for i in str(n):
        t += int(i)
    print "2^%d = %d = %d" %(x, n, t)