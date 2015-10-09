import time

def func(num):
    string = ""
    k = 1
    while len(string)<num:
        string += str(k)
        k += 1
    lel = []
    le = 1
    while le<num:
        lel.append(le)
        le *= 10
    ans = 1
    ansl = [int(string[i-1]) for i in lel]
    for i in ansl:
        ans *= i
    print ans
    
start = time.time()
func(1000000)
print time.time() - start