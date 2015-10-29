def euler010(n):
    squrt = int(n**0.5)
    
    bool_list = [True] * n

    def mark(function_list, x):
        for i in xrange(x*x, len(function_list), x):
            function_list[i] = False
    
    bool_list[0] = False
    bool_list[1] = False
    
    for j in xrange(2, squrt+1):
        mark(bool_list, j)
    
    return sum(s for s in xrange(0, len(bool_list)) if bool_list[s])

