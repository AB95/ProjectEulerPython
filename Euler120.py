

tot = 0
for a in xrange(3, 1001):
    if a % 2 == 0:
        tot += (a-2)*a
    elif a % 2 == 1:
        tot += (a-1)*a
print tot