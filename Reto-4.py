def crear_usuarios (empleados: list):
     usuarios_codigo=[]
     usuarios_nombre=[]
     lista_usuarios=[]

     for empleado in empleados:
          cadena=[]
          usuarios_codigo.append(empleado['cod_empleado'])
         
          cadena.append(empleado['nombre1'][0])
          if empleado['nombre2'] == '':
               cadena.append(empleado['nombre1'][1])
          else:
               cadena.append(empleado['nombre2'][0])
          cadena.append(empleado['fecha_nacimiento'][-2:])
          cadena.append(empleado['apellido1'][0])
          if empleado['apellido2'] == '':
               cadena.append(empleado['apellido1'][1])
          else:
               cadena.append(empleado['apellido2'][0])

          buscar_cadena=''.join(cadena)
          
          buscar_cadena=''.join((map(lambda x: x.upper(), buscar_cadena)))
          
          for usuario in lista_usuarios:
               contador=0
               while usuario == buscar_cadena:
                    contador += 1
                    buscar_cadena=''.join(cadena)+str(contador)
                    
          
          lista_usuarios.append(buscar_cadena)
          usuarios_nombre.append((empleado['cod_empleado'],buscar_cadena))
     print("##")
     print("------------------------")
     print(lista_usuarios)     
     print("------------------------")
     print("##")
     
     return usuarios_nombre

empleados1=[{'cod_empleado': 'EMPL_001', 'nombre1':'Rodrigo', 'nombre2': 'Andres', 'apellido1':'Estupiñan', 'apellido2': 'Zapata','fecha_nacimiento': '23-10-1993'}, 
            {'cod_empleado': 'EMPL_002', 'nombre1':'Ramiro', 'nombre2': 'Alberto', 'apellido1':'Espitia', 'apellido2': 'Zambrano','fecha_nacimiento': '01-02-1993'},
            {'cod_empleado': 'EMPL_003', 'nombre1':'Rene', 'nombre2': 'Alejandro', 'apellido1':'Echavarria', 'apellido2': 'Zamudio','fecha_nacimiento': '02-09-1993'}]

empleados2=[{'cod_empleado': 'EMPL_001', 'nombre1':'Rodrigo', 'nombre2': 'Andres', 'apellido1':'Estupiñan', 'apellido2': 'Zapata','fecha_nacimiento': '23-10-1993'},
            {'cod_empleado': 'EMPL_002', 'nombre1':'Javier', 'nombre2': '', 'apellido1': 'Guzman','apellido2': '', 'fecha_nacimiento': '01-02-1987'}, 
            {'cod_empleado': 'EMPL_003', 'nombre1': 'Rene', 'nombre2': 'Alejandro', 'apellido1': 'Echavarria', 'apellido2':'Zamudio', 'fecha_nacimiento': '02-09-1982'}]

print(crear_usuarios(empleados1))
print(crear_usuarios(empleados2))