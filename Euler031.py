

tot = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*tot

for i in coins:
    for j in xrange(i, tot+1):
        ways[j] += ways[j - i]

print ways[-1]