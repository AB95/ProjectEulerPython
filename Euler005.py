import time

@profile
def func():
    start = time.time()
    u = 20
    finished = False
    x = [19, 18, 17, 16, 15, 14, 13, 12, 11]
    
    while not finished:
        if u%x[0]==0 and u%x[1]==0 and u%x[2]==0 and u%x[3]==0 and u%x[4]==0 and u%x[5]==0 and u%x[6]==0 and u%x[7]==0 and u%x[8]==0:
             print u
             finished = True
        else:
            u += 20
    end = time.time()
    print end-start

func()