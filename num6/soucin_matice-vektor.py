m = [[1, 2, 3],[4, 5, 6]]
v = [1, 2, 3]
def transpozice(n):
    [[r[i] for r in n] for i in range(len(n[0])]
vysledek = sum ([(soucin(m[i],transpose(v[0]) for i in range(len(m)])
