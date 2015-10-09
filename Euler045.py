

pentlist = set([(i * (3*i - 1))/2 for i in xrange(1, 1000000)])
hexlist = [i*(2*i-1) for i in xrange(1, 1000000)]

for i in hexlist:
    if i in pentlist:
        if i>40755:
            print i
