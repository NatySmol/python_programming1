N = int(input())
seznam = []
for n in range (N):
    n = int(input())
    seznam.append(n)
    
M = int(input())       
for k in range(M):
    k = int(input())
    seznam.append (k)
    
for i in range(1,len(seznam)):
    a = seznam[i]
    j = i

    while j>0 and seznam[j-1]>a:
        seznam[j]=seznam[j-1]
        j-=1
    seznam[j]=a

for i in range(0, len (seznam)):
    print(seznam[i])        

