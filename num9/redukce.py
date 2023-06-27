def red(s, f):
    temp = s[0]
    for i in range(1, len(s)):
        temp = f(temp, s[i])
    return temp
