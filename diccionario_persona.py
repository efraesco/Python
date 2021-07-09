personas = dict(
    persona1 = dict(
            nombres ="Leonardo Jose",
            apellidos="Caballero Garcia",
            cedula="26938401",
            fecha_nacimiento="03/12/1980",
            lugar_nacimiento="Maracaibo, Zulia, Venezuela",
            nacionalidad="Venezolana",
            estado_civil="Soltero",
            experiencia_laboral = dict(
                    experiencia1 = dict(
                        empresa = 'Empresa1',
                        tiempo_experiencia = 1
                    ),
                    experiencia2 = dict(
                        empresa = 'Empresa2',
                        tiempo_experiencia = 0.5
                    ),
                    experiencia3 = dict(
                        empresa = 'Empresa3',
                        tiempo_experiencia = 1.5
                    )
                )),
    persona2 = dict(
            nombres ="Pepito Jose",
            apellidos="Lara Garcia",
            cedula="26876543",
            fecha_nacimiento="03/09/1985",
            lugar_nacimiento="Bogotá, Colombia",
            nacionalidad="Colombiano",
            estado_civil="Soltero",
            experiencia_laboral = dict(
                    experiencia1 = dict(
                        empresa = 'Empresa1',
                        tiempo_experiencia = 0.3
                    ),
                    experiencia2 = dict(
                        empresa = 'Empresa2',
                        tiempo_experiencia = 0.3
                    ),
                    experiencia3 = dict(
                        empresa = 'Empresa3',
                        tiempo_experiencia = 0.8
                    )
                )),
    persona3 = dict(
            nombres ="Luz Milena",
            apellidos="Flores Penagos",
            cedula="876534278",
            fecha_nacimiento="05/11/1988",
            lugar_nacimiento="Pitalito, Huila, Colombia",
            nacionalidad="Colombiana",
            estado_civil="Casada",
            experiencia_laboral = dict(
                    experiencia1 = dict(
                        empresa = 'Empresa1',
                        tiempo_experiencia = 2
                    ),
                    experiencia2 = dict(
                        empresa = 'Empresa2',
                        tiempo_experiencia = 1.5
                    ),
                    experiencia3 = dict(
                        empresa = 'Empresa3',
                        tiempo_experiencia = 0.2
                    )
                )
            )
)

for item in personas:
    print ("Nombre", personas[item]['nombres'], personas[item]['apellidos'], sep="|")

