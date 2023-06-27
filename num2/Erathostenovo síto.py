N = int(input())
s=[True]*(N+1)

for i in range(2, len(seznam)):  
    if seznam[i]:
        print(i)
        for j in range (i, len(seznam), i):
            seznam[j]= False
        
         
         
                
