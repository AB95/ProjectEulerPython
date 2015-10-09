

def func():
    pentlist = [(i * (3*i - 1))/2 for i in xrange(1, 10000)]
    pents = set(pentlist)    
    
    def isPent(i, pentlist):
        if i in pents:
            return True
        return False
    
    Dmax = []
    leng = len(pentlist)
    for i in xrange(leng):
        print i
        for j in xrange(i+1, leng):
            pent1 = pentlist[i]
            pent2 = pentlist[j]
            if isPent(pent1 + pent2, pents) and isPent(pent2 - pent1, pents):
                Dmax.append(abs(pent2 - pent1))
    print min(Dmax)
func()