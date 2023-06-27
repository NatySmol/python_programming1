s = [1, 2, 3, 4]
def red(s, f):
    temp = s[0]
    for i in range(1, len(s)):
        temp = f(temp, s[i])
    return temp

def prvni_nenulovy(s):
    def f(x, y):
        if x != 0:
            return x
        else:
            return y
        
    
