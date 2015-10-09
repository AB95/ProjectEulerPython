from time import time
def func():
    start = time()
    from math import factorial
    
    m = 20    
    n = 20
    rekt = m + n
    
    ans = factorial(rekt)/(factorial(m)*factorial(n))
    end = time()
    print end-start
    print ans
func()

#def func():
#    start = time()
#    def fact(x):
#        t = 1
#        for i in xrange(x, 0, -1):
#            t *= i
#        return t
#        
#    def problem(x):
#        ans = fact(2*x)/(fact(x)**2)
#        return ans
#    
#    print problem(20)
#    end = time()
#    print end-start
#func()