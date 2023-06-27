seznam = [2, 5, 1, 7, 6, 0]
n = len(seznam)
for j in range (n-1):
    for i in range(n-1 - j):
        if seznam [i] > seznam[i+1]:
            seznam[i], seznam[i+1] = seznam [i+1], seznam [i]
    print(seznam)
