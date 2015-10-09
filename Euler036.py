import time

#@profile
def flunc():
#    @profile    
    def func(i):
        j = int(str(i)[::-1])
        
        return [i, j]
    
    def func2(i):
        k = int(bin(i)[2:])
        l = int(str(k)[::-1])
        
        return [k, l]
    
    start = time.time()
    tot = 0
    for i in xrange(1, 1000000, 2):
        lst = (func(i))
        if lst[0] == lst[1]:
            lst2 = (func2(i))
            if lst2[0] == lst2[1]:
                tot += lst[0]
    print tot
    print time.time() - start
flunc()