from math import sqrt

def findSides(i):
    sides = 1
    for a in xrange(i/2):
        for b in xrange(i/3, i):
            c = sqrt(a**2 + b**2)
            if c + a + b == i and a and b and c:
                sides += 1
    return sides
                
ans = 0
num = 0
for i in xrange(1001):
    if findSides(i) > num:
        num = findSides(i)
        ans = i
        
print "The answer is %d with %d answers!" %(ans, num)