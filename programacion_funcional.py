# programacion funcional

def suma(val1=0,val2=0):
    return val1+val2

def programacion_funcional(funcion,val1=0,val2=0):
    return funcion(val1,val2)

resultado=programacion_funcional(suma,10,20)
print(resultado)