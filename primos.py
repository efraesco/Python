# Generar los 100 primeros numeros primeros

for x in range(2,101):
    contar_divisores = 0

    for y in range(1,x+1):
        if x % y == 0:
            contar_divisores = contar_divisores + 1
    
    if contar_divisores == 2:
        print(x, "," )
    
    
    