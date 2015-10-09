

top = 0
for a in xrange(100):
    for b in xrange(100):
        power = a ** b
        add = sum(int(i) for i in str(power))
        if add > top:
            top = add
print top