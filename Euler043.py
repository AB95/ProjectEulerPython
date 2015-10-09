from itertools import permutations

permuts = [i for i in permutations("0123456789")]
for i in xrange(len(permuts)):
    string = ""
    for j in permuts[i]:
        string += j
    permuts[i] = string
permuts = list(set(permuts))
    
def isDiv(x):
    string = str(x)
    array = [2, 3, 5, 7, 11, 13, 17]
    for i in xrange(len(array)):
        if int(string[i+1:i+4]) % array[i] != 0:
            return False
    return True

print sum([int(i) for i in permuts if isDiv(i)])