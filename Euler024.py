import itertools as it
import time

def func():
    start = time.time()
    print "".join([i for i in itp("0123456789")][999999])
    print time.time() - start
    
func()