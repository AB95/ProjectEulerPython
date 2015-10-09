import Euler10

def func(top):
    primes = Euler10.func(top)
    
    for i in primes[::-1]:
        c = 1
        while pow(10, c, i) - 1 != 0:
            c+=1
        if i-c == 1:
            return i
    
print func(1000)