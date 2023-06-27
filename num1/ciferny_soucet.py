n= int(input())
soucet = 0
while n>0:
    print (n)
    digit= n%10
    soucet +=digit
    n//=10
print (soucet)
