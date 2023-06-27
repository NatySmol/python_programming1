seznam = []
while True:
    i = int(input()) 
    if i!=-1:
        seznam.append (i)
    elif i ==-1:
        k = int(input())
        break
for j in range(0,k - 1):
    seznam.remove(max(seznam))
    k-=1
print(max(seznam))
