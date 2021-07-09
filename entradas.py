def validador(rango_inicial, rango_final):
	entrada = True
	while entrada == True:
		valor= float(input("ingresa una nota entre " + str(rango_inicial) + " y " + str(rango_final) +": "))
		if valor < rango_inicial or valor > rango_final:
			entrada=True
		else:
			entrada=False
	return entrada

entrada=validador(1.0,5.0)
