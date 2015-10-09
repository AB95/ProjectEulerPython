import Euler10


def func():
    primes2 = Euler10.func(7072)
    primes3 = Euler10.func(369)
    primes4 = Euler10.func(85)

    lst = set()
    for i in primes2:
        for j in primes3:
            for k in primes4:
                x = i**2 + j**3 + k**4
                if x < 50000000 and x not in lst:
                    lst.add(x)

    return len(lst)

print func()