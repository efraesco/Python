#suma = lambda *args : sum (args)
suma = lambda **kwargs : sum(kwargs.values())
calcular=suma(one=1,two=2,three=3)
print(calcular)



#calcular=suma(10,20,30,40,50)
#print(calcular)

#resultado = 'True' if calcular == 150 else 'False'
#print (resultado)
