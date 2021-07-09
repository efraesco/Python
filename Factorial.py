# Factorial de un numero
def factorial(numero):
    resultado = 1
    for x in range(1,numero+1):
        resultado *= x
    return resultado

def factorialWhile(numero):
    resultado=1
    contador=0
    while contador < numero:
        contador += 1
        resultado *= contador
    return resultado

print(factorial(10))
print(factorialWhile(10))

