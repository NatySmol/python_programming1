n = int(input())
seznam = [f"{a}*{b} = {a*b}" for a in range(1, n+1) for b in range (1, n+1)]
for s in seznam:
    print(s)

