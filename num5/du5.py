def prvocisla(n):
    cisla = [True]*(n+1)
    s = []
    for i in range(2, n+1):
        if cisla[i]:
            s.append(i)
            for j in range(2*i, n+1, i):
                cisla[j]=False
    return s
