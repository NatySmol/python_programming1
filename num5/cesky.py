#!/usr/bin/env python3

zakladni = [
    None, "jedna", "dva", "tři", "čtyři",
    "pět", "šest", "sedm", "osm", "devět",
    "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
    "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
]

desitky = [
    None, None, "dvacet", "třicet", "čtyřicet",
    "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
]

def cesky(x):
    # Zde se postupně skládají slova výsledku
    out = []

    # Vybere správný tvar slova odpovídající počtu: [1, 2-4, 5+]
    def ohybej(x, var):
        if x == 1:
            i = 0
        elif x <= 4:
            i = 1
        else:
            i = 2
        out.append(var[i])

    # Zpracuje čísla v rozsahu 1 až 999
    def stovky(y):
        if y >= 100:
            s, y = y // 100, y % 100
            if s == 2:
                # 200 má zcela speciální tvar
                out.append("dvě")
                out.append("stě")
            else:
                if s > 1:
                    out.append(zakladni[s])
                ohybej(s, ["sto", "sta", "set"])
        if y >= 20:
            d, y = y // 10, y % 10
            out.append(desitky[d])
        if y > 0:
            out.append(zakladni[y])

    if x == 0:
        return "nula"

    if x >= 1000000000:
        return "moc"

    # Miliony
    if x >= 1000000:
        m, x = x // 1000000, x % 1000000
        if m > 1:
            stovky(m)
        ohybej(m, ["milion", "miliony", "milionů"])

    # Tisíce
    if x >= 1000:
        t, x = x // 1000, x % 1000
        if t > 1:
            stovky(t)
        ohybej(t, ["tisíc", "tisíce", "tisíc"])

    # Zbytek
    stovky(x)
    return " ".join(out)

# Testovací program
while True:
    print(cesky(int(input())))
