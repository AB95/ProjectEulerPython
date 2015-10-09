from time import time

def func():
    i = 101010102
    erg = False

    while i<138902663:
        if str(i**2)[::2] == "123456789":
            break
        i += 1

    return i*10

start = time()
print func()
print time()-start