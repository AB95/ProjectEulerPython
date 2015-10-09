

i = -1
leng = 3
inc = 2
tot = 1
num = 1
while leng <= 1001:
    i += 1
    if i == 4:
        i = -1
        leng += 2
    elif i <= 4:
        num += leng -1
        tot += num
    print tot