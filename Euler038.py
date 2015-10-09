

def func():
    def isPan(x):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in nums:
            if str(i) not in x:
                return False
        return True
    
    maxNum = 0
        
    for i in xrange(10000):
        string = str(i)
        for j in xrange(2, 10):
            string += str(i*j)
            if len(string) == 9:
                if int(string) > maxNum and isPan(string):
                    maxNum = int(string)
    print maxNum
    
func()
                    
