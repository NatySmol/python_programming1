max1,max2 = 0,0

while True:
    i = int(input())
    if i == -1:
        break
    if max1<i:
        max1,max2 = i,max1
    elif max2<i:
        max2 = i

print(max2)
