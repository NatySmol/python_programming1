def min2(a, b)
     if a<b:
         return a
    return b
def min3 (a, b, c)
    return min2(min2(a,b), c)
def mi4(a, b, c, d)
    return min2(min3(a, b, c), d)
