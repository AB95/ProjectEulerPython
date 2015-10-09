import priimes

def func():
    primes = priimes.func(100000)
    squares = [2 * (i**2) for i in xrange(100000)]
    
    erg = True
    x = 7
    while erg == True:
        x+=2
        if x in primes:
            x+= 2
        else:
            i = 0
            while primes[i] < x:
                j = 0
                while squares[j] < x:
                    if primes[i] + squares[j] == x:
                        erg = False
                    j += 1
                i += 1
            if erg == False:
                erg = True
            else:
                print x
                break

func()