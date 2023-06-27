n = int(input())
s = 0
i= 0
while n!=0:
    s += (n%2) *(10**i)
    n//=2
    i+=1
print(s)
