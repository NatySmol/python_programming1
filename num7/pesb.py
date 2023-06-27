from collections import defaultdict
kgramy = defaultdict (int)
k = 3
for radek in open("pes.txt", encoding = "utf - 8"):
    for i in range (len(radek) - k):
        kgramy[radek[i:i+k]] +=1
seznam=[(hodnota, klic for klic , hodnota in kgramy.items()]
seznam = sorted(seznam)
for h, k in seznam:
    print(k, h)

