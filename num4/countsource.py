a = [0]*10
while True:
    i = int(input())
    if i == -1:
        break
    a[i-1] += 1

print(a)
