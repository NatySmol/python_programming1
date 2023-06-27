max = -1
maxindex= 0
druhenejvetsi = -1
maxdruhyindex=0
index= 0
while True:
    n = int(input())
    if n == -1:
        break
    if max < n:
        max, druhenejvetsi = n, max
        #prohodit indexy
    elif druhenejvetsi < cislo:
        druhenejvetsi = cislo
        #priradit spravny index
        
print (druhenejvetsi)
        
