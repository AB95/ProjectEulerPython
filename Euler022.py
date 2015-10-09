def Euler22(text):
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
                   
            return dic[let.upper()]
    
    def findScore(name):
        x = 0
        for i in name:
            x += let2Num(i)
        return x
    
    f = file(text, "r")
    names = f.readline().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]
    names = sorted(names)
    print names.index("COLIN")
    scores = [findScore(i) for i in names]
    print scores[936]
    scores = [scores[i]*(i+1) for i in xrange(0, len(scores))]
    print scores[936]
    print sum(scores)
    f.close()

Euler22("/home/bouch/Downloads/Euler22.txt")