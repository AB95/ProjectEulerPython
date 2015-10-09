import time

def func():
    def let2Num(let):
        dic = {"A" : 1,
               "B" : 2,
               "C" : 3,
               "D" : 4,
               "E" : 5,
               "F" : 6,
               "G" : 7,
               "H" : 8,
               "I" : 9,
               "J" : 10,
               "K" : 11,
               "L" : 12,
               "M" : 13,
               "N" : 14,
               "O" : 15,
               "P" : 16,
               "Q" : 17,
               "R" : 18,
               "S" : 19,
               "T" : 20,
               "U" : 21,
               "V" : 22,
               "W" : 23,
               "X" : 24,
               "Y" : 25,
               "Z" : 26}
               
        return dic[let]
        
    def tri(word):
        j = 0
        for i in word:
            j += let2Num(i)
        return j
    
    def isTri(word):
        x = 1
        y = 1
        num = tri(word)
        while x < num:
            y += 1
            x += y
        if x == num:
            return True
    
    f = open("/home/bouch/Downloads/Euler42.txt", "r")
    counter = 0    
    for i in f:
        currentword = i.split('","')
    for i in currentword[1:-1]:
        if isTri(i):
            counter += 1
    if isTri(currentword[0][1:]):
        counter += 1
    if isTri(currentword[-1][:-1]):
        counter += 1
    f.close()
    return counter

start = time.time()
print func()
print time.time() - start