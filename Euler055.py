
def func(topNum, itNum):
    def isLychrel(x, itNum):
        i = 0
        while i<itNum:
            i += 1
            x += int(str(x)[::-1])
            if x == int(str(x)[::-1]):
                return True
            i += 1
        return False
        
    return len([i for i in xrange(topNum) if not isLychrel(i, itNum)])
    
print func(10000, 50)
            