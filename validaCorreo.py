# Validar correo e incorporar en un diccionario

listaCorreosValidos = list()
for _ in range(3):
    # Validar si el correo es válido y obtener el usuario y el dominio
    correo = input ('Ingresar un correo: ')

    # Operador Ternario
    validarCorreo = True if correo.count("@")==1 else False
    resultado = "válido" if (validarCorreo) else "inválido"

    if (validarCorreo):
        elementosCorreo = correo.split ("@")

        diccionarioCorreo = { "usuario": elementosCorreo[0], "dominio": elementosCorreo[1]}

        # Adicionar el diccionario a la lista
        listaCorreosValidos.append(diccionarioCorreo)

    print(f"El correo {correo} es {resultado}")

print(listaCorreosValidos)

# convierto la lista en tupla para no ser más modificada
listaCorreosValidos = tuple(listaCorreosValidos)

# Recorrido de la lista y el diccionario
for i, elemento in enumerate(listaCorreosValidos):
    print(f'Correo válido No. {i+1}')
    for llave, valor in elemento.items():
        print(llave,valor, sep=":")

