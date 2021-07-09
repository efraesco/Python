# Serie Fibonacci
#   0   1   2   3   4   5   6   7   8   9   10 
#   0   1   1   2   3   5   8   13  21  34  55

def fibonacci_recursivo(numero):
    if numero == 0: return 0
    if numero == 1: return 1
    if numero > 1:
        return fibonacci(numero-1) + fibonacci(numero-2)
        
        
def fibonacci(numero):
    primero = 0
    anterior = 1
    if numero==0: return primero
    if numero==1: return anterior

    if numero > 1:
        contador = 1
        resultado = 0
        while contador < numero:
            resultado = primero + anterior
            primero = anterior
            anterior = resultado
            contador += 1
        return resultado

    
#contador=0
#while contador <= 100:
#    print("fibonacci de", contador," es igual a", fibonacci(contador))
#    contador += 1

# print(fibonacci_recursivo(100))   

numero=10000
numstr=str(numero)
alreves=""
for i in range(len(numstr)-1, -1, -1):
    alreves = alreves + numstr[i]
numalreves =int(alreves)
if numero == numalreves: print ("Es capicuo")
else: print("No es capicuo")

    