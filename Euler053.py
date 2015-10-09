from math import factorial

def nCr(n):
    nums = []
    for r in xrange(n+1):
        x = factorial(n)/(factorial(r)*factorial(n-r))
        if x > 1000000:
            nums.append(x)
    return nums 

array = []
for j in xrange(101):
    array.extend(nCr(j))
print len(array)