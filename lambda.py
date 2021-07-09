suma = lambda x,y : x+y
resta = lambda x,y : x-y
multiplica = lambda x,y : x*y
division = lambda x,y: x/y

def operaciones(funcion,x=0,y=0):
    if funcion == '+':
        return suma(x,y)
    elif funcion == '-':
        return resta(x,y)
    elif funcion == '*':
        return multiplica(x,y)
    elif funcion == '/':
        return division(x,y)


funcion='/'
resultado= operaciones(funcion,50,20)
print(resultado)
