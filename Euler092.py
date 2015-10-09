
def func(top):
    def is89(i):
        while i != 89:
            i = sum(int(j)**2 for j in str(i))
            if i == 1:
                return False
        return True
    
#    others = []
    count = 0    
    
    for i in xrange(1, top):
        if is89(i):
#            others.append(i)
            count += 1
    print count
    
func(10000000)