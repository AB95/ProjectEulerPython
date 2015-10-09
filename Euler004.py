import time

#@profile
def func():
    start = time.time()
    x = 999
    y = 999
    
#    @profile
    def isPal(f):
        if str(f) == str(f)[::-1]:
            return True
    
    while y>800:
        while x>800:
            if isPal(x*y):
                print x*y
                y = 600
            x -= 1
        x = 999
        y-=1
        print y
    
    end = time.time()
    print end-start

func()