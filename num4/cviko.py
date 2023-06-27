n = int(input())
k = 0
s = 0
while n > 0:
    p = n%2
    s= p*(2**k)
    k+=1
    n//=10
print(s)
