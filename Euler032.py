

def func():
    mults = []
    
    def isPan(x):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in nums:
            if str(i) not in x:
                return False
        return True
            
    for i in xrange(10000):
        for j in xrange(100):
            prod = i * j
            string = str(i) + str(j) + str(prod)
            if len(string) == 9:
                if isPan(str(i) + str(j) + str(prod)) and prod not in mults:
                    mults.append(prod)
    
    print sum(mults)
    
func()