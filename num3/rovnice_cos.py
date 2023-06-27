from math import *
e= 10**(-10)
left = -5
right = 5
while abs(left-right) > e:
    stred = (left + right)/2
    if abs(cos(stred) -stred) <e :
        print(stred)
        break
    elif (cos(stred)-stred) >e:
        left = stred
    else:
        right = stred
    print(stred)
