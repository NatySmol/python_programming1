a = int(input())
b = int(input())
c = int(input())
d = int(input())
citatel = a*d + c*b
jmenovatel = b*d

y = citatel
z = jmenovatel
while z != 0:
    y,z= z,y%z

citatel //= y
jmenovatel //= y
print (citatel)
print (jmenovatel)

