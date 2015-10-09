

def permuted(x):
    sett = set([i for i in str(x)])
    for i in xrange(2, 7):
        if set([i for i in str(x*i)]) != sett:
            return False
    return True
    
boo = False
i = 0
while boo == False:
    i += 1
    if permuted(i):
        boo = True
print i