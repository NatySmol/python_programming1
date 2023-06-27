n = int(input())
levy = 0
p = n
while levy <= p:
    stred = (levy + p)//2
    if stred**2 == n:
        print ("nasli jsme", stred)
        break
    elif stred**2 < n:
        levy = stred + 1
    else:
        p = stred -1
else:
    print("nic jsme nenasli")
    
