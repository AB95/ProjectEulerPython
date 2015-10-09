import time

def func():
    start = time.time()
    a = 1
    b = 1
    c = 1
    
    while c<1000:
        if a < b and b < c and a+b+c == 1000 and a**2 + b**2 == c**2:
            print str(a) + ", " + str(b) + ", " + str(c)
        else:
            if b-a<200:
                if c-b < 200:
                    c += 1
                    if a < b and b < c and a+b+c == 1000 and a**2 + b**2 == c**2:
                        print str(a) + ", " + str(b) + ", " + str(c)
                        print a*b*c
                        break
                else: 
                    c = b
                    b += 1
            else:
                b = a
                a += 1
    end = time.time()
    print end-start
func()