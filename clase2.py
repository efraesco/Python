# Algoritmo para calcular el promedio de 3 notas

# Funcion
def calcular_promedio(nota_1,nota_2,nota_3):
    suma_notas = sum ((nota_1, nota_2, nota_3))
    promedio_notas = round(suma_notas / len( (nota_1,nota_2,nota_3) ), 2)
    return promedio_notas

# Principal
nota1=3.5
nota2=4.0
nota3=5.0
resultado=calcular_promedio(nota1, nota2, nota3)
maxima_nota=max(nota1, nota2, nota3)
minima_nota=min(nota1, nota2, nota3)

#Resultado
print ("El promedio de las sguientes notas", nota1, nota2, nota3, "es igual a ", resultado)
print ("La nota máxima es", maxima_nota)
print ("La nota mínima es", minima_nota)
