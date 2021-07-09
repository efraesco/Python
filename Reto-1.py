def notas_finales_estudiante(codigo, notaQuiz1=0, notaTaller1=0, notaParcial1=0, notaQuiz2=0, notaTaller2=0, notaParcial2=0, notaQuiz3=0, notaTaller3=0, notaParcial3=0):
    
    
    # Calcular peso de las notas por concepto
    
    # Corte1
    SumaNotasCorte1 = sum ( (notaQuiz1*0.25, notaTaller1*0.15, notaParcial1*0.60) )
    
    # Corte2
    SumaNotasCorte2 = sum ( (notaQuiz2*0.25, notaTaller2*0.15, notaParcial2*0.60) )
        
    # Corte3
    SumaNotasCorte3 = sum ( (notaQuiz3*0.25, notaTaller3*0.15, notaParcial3*0.60) )
    
    # Calcular Notas Corte en escala 0 a 5
    nota_corte_1=round (SumaNotasCorte1 * 0.05,2)
    nota_corte_2=round (SumaNotasCorte2 * 0.05,2)
    nota_corte_3=round (SumaNotasCorte3 * 0.05,2)
    
    # Calcular Nota final
    nota_final = sum ( (SumaNotasCorte1 * 0.25, SumaNotasCorte2 * 0.30, SumaNotasCorte3 * 0.45 ) )
    
    # Calcular Nota final en escala 0 a 5
    nota_final_semestre = round (nota_final * 0.05, 2)
           
    
    return f"Estudiante {codigo} sus notas son las siguientes: Corte 1: {nota_corte_1}, Corte 2: {nota_corte_2}, Corte 3: {nota_corte_3} y su Nota Final en el semestre es: {nota_final_semestre}"
    #return "Estudiante {} sus notas son las siguientes: Corte 1: {}, Corte 2: {}, Corte 3: {} y su Nota Final en el semestre es: {}".format(codigo, nota_corte_1, nota_corte_2, nota_corte_3, nota_final_semestre)
    
print ( notas_finales_estudiante('EST_RETO_1', 80.5, 90.0, 70.5, 35.4, 95.0, 80.5, 80.5, 82.5, 75.5) )
print("{:.2f}".format(nota_final))


    