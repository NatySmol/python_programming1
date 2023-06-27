max = -1
druhenejvetsi = -1
while True:
    n = int(input())
    if n == -1:
        break
    if max < n:
        max, druhenejvetsi = n, max
    elif druhenejvetsi<cislo:
        druhenejvetsi = cislo
        
print (druhenejvetsi)
        
