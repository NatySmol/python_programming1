n= int(input())
d=2 #dělitel, začínám na 2 až n-1
mam_delitele = False
while d<n:
    if n%d==0:
        print("čislo", n, "je delitelne", d)
        mam_delitele = True
        break
    d+= 1
if not mam_delitele:
    print("cislo", n, "je prvočislo")
    
