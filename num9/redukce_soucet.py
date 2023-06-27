s = [1, 2, 3, 4]
def red(s, f):
    temp = s[0]
    for i in range(1, len(s)):
        temp = f(temp, s[i])
    return temp

soucet = red(s, lambda x, y: x + y )
print(soucet)
