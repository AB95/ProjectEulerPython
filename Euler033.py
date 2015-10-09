array = []

for j in xrange(10, 100):
    for i in xrange(10, j):
        for k in str(i):
            if k in str(j) and k != "0":
                larray = [x for x in str(i) if x != k]
                marray = [x for x in str(j) if x != k]
                if larray and marray:
                    l = int("".join(larray))
                    m = int("".join(marray))
                    if l and m and l!=m:
                        if float(l)/m == float(i)/j:
                            array.append((i, j))
                    
top = 1
bot = 1
for i in xrange(len(array)):
    top *= array[i][0]
    bot *= array[i][1]

def divs(i):
    divs = []
    for j in xrange(2, i):
        if i%j == 0:
            divs.append(j)
    return divs

#fract = [top, bot]
#print divs(10)

def simp(lst):
    div = divs(lst[1])
    for i in divs(lst[0]):
        if i in div and i and div:
            simp([lst[0]/i, lst[1]/i])
    print lst
    
simp(fract)
        