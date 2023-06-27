n = int(input())
d=2
while d <= (n//2):
    if n%d == 0:
        print("Ćıslo", n, "je deliteln e", d)
        break
    d += 1
else:
    print("Ćıslo", n, "je prvoćıslo")
