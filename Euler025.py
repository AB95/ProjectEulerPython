import time

def func():
    xterm = 1
    yterm = 1
    x = 1
    y = 1
    while True:
        if len(str(x)) == 1000:
            return xterm+yterm
        elif len(str(y)) == 1000:
            return yterm+yterm
        x += y
        xterm += 1
        y += x
        yterm += 1
 
start = time.time()   
print func()
end = time.time()
print len(str(func()))
print end - start