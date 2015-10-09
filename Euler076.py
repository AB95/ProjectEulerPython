tot = 100
coins = [i for i in xrange(1, tot)]
ways = [1] + [0]*tot

for i in coins:
    for j in xrange(i, tot+1):
        ways[j] += ways[j - i]

print ways[-1]