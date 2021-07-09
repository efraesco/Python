def analisis_estudiante(solicitud: dict) -> dict:
    resultado_analisis=False
    if solicitud["activo"] == "A":
        if solicitud["nota_final_semestre_1"] > 0 and solicitud["nota_final_semestre_2"] > 0 and solicitud["nota_final_semestre_3"] > 0 and solicitud["nota_final_semestre_4"] > 0:
            if solicitud["adeuda_semestre"] == 'N':
                    if solicitud["tiene_multa"] == 'N':
                        if solicitud["proceso_academico"] == 'N':
                            if sum ( (solicitud["nota_final_semestre_1"],solicitud["nota_final_semestre_2"],solicitud["nota_final_semestre_3"],solicitud["nota_final_semestre_4"]) )/4 > 4.0:
                                resultado_analisis = True
    return {"cod_estudiante": solicitud["cod_estudiante"],"resultado_analisis": resultado_analisis}


estudiante = {
 'cod_estudiante': 'EST_01',
 'nota_final_semestre_1': 3.56,
 'nota_final_semestre_2': 4.64,
 'nota_final_semestre_3': 4.0,
 'nota_final_semestre_4': 4.97,
 'adeuda_semestre': 'N',
 'tiene_multa': 'N',
 'proceso_academico': 'N',
 'activo': 'A'
 }

print (analisis_estudiante(estudiante))