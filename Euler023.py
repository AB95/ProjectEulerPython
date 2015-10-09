def func():
    def isAbun(i):
        if sum(j for j in xrange(1, i) if i % j == 0) > i:
            return True
        return False

    def isAbunSum(i, abuns, abunsSet):
        for j in abuns:
            if j > i:
                return False
            elif i - j in abunsSet:
                return True
        return False

    abuns = [i for i in xrange(1, 28124) if isAbun(i)]
    abunsSet = set(abuns)

    print sum(i for i in xrange(1, 28124) if not isAbunSum(i, abuns, abunsSet))


func()
