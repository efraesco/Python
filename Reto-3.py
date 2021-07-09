import pprint as pp  

def evaluar_deuda (clientes: dict):
    
    clientes_beneficiados = dict()
    
    #diccionario_por_deuda = dict()
        
    for cliente in clientes.values():
        print(cliente['cod_cliente'])
        
        deuda_total=0
        for deuda in cliente['valores_deuda'].values():
            print(deuda)
            calculo = deuda['valor_deuda'] * (1 + (deuda['tasa_interes']/100) ) 
            print (calculo)
            deuda_total = deuda_total + calculo
            
        deuda_total = round (deuda_total,2)
        #diccionario_por_deuda[cliente['cod_cliente']]=deuda_total
        cliente['deuda_total']=deuda_total
        print("deuda total", cliente['deuda_total'])
                
    for cliente in clientes.values():
        if cliente['acuerdo_pago'] == False:
            if len(clientes_beneficiados) < 2:
                key = 'cliente' + str(len(clientes_beneficiados)+1)
                #print(key)
                clientes_beneficiados[key] = dict(cod_cliente = cliente['cod_cliente'], valor_deuda = cliente['deuda_total'], condona = False, financia= False)
            else:
                deuda = cliente ['deuda_total']
                for item in clientes_beneficiados.values():
                    if item['valor_deuda'] > deuda:
                        item['cod_cliente'] = cliente['cod_cliente']
                        item['valor_deuda'] = deuda
                        break
        
    if len(clientes_beneficiados) == 2:
        if clientes_beneficiados['cliente1']['valor_deuda'] < clientes_beneficiados['cliente2']['valor_deuda']:
            clientes_beneficiados['cliente2']['financia']=True
            if clientes_beneficiados['cliente1']['valor_deuda'] < 1000000.00:
                clientes_beneficiados['cliente1']['condona']=True
            else: clientes_beneficiados['cliente1']['financia']=True

        else:
            clientes_beneficiados['cliente1']['financia']=True
            if clientes_beneficiados['cliente2']['valor_deuda'] < 1000000.00:
                clientes_beneficiados['cliente2']['condona']=True
            else:
                clientes_beneficiados['cliente2']['financia']=True
            
        clientes_beneficiados['cliente1']['valor_deuda']=str(clientes_beneficiados['cliente1']['valor_deuda'])
        clientes_beneficiados['cliente2']['valor_deuda']=str(clientes_beneficiados['cliente2']['valor_deuda'])
        
    elif len(clientes_beneficiados) == 1:
        if clientes_beneficiados['cliente1']['valor_deuda'] < 1000000.00:
            clientes_beneficiados['cliente1']['condona']=True
        else:
            clientes_beneficiados['cliente1']['financia']=True

        clientes_beneficiados['cliente1']['valor_deuda']=str(clientes_beneficiados['cliente1']['valor_deuda'])

    else:
        return dict (mensaje = "No se encontraron clientes para ofrecer negociación") 
      
    
    return clientes_beneficiados
    
    #     if cliente['acuerdo_pago'] == False:
    #         if deuda_total < 10000000.00:
    #             cliente['condona']=True
    #             cliente['financia']=False
    #         elif deuda_total > 1000000.00:
    #             cliente['condona']=False
    #             cliente['financia']=True
    #     else:
    #         return {"mensaje": "No se encontraron clientes para ofrecer negociación"}
       
    # diccionario_ordenado = sorted(diccionario_por_deuda.items(), key=lambda x: x[1])
    
    # diccionario_retorno = dict()
    # for i in range(2):
    #     for cliente in clientes.values():
    #         if cliente['cod_cliente'] == diccionario_ordenado[i][0]:
    #             #print(diccionario_ordenado[i][0])
    #             cadena_cliente= 'cliente'+str(int(not i)+1)
    #             #print(cadena_cliente)
    #             diccionario_retorno[cadena_cliente] = { 'cod_cliente': cliente['cod_cliente'], 'valor_deuda': cliente['deuda_total'], 'condona': cliente['condona'], 'financia': cliente['financia'] }
    #             #pp.pprint(diccionario_retorno)
    
    # #print(diccionario_retorno)
    # nuevo_diccionario=dict()
    # nuevo_diccionario['cliente1']= dict(diccionario_retorno.get('cliente1'))
    # nuevo_diccionario['cliente2']= dict(diccionario_retorno.get('cliente2'))
             
    # return nuevo_diccionario



{'cliente1': {'cod_cliente': 'CLT_003', 'valor_deuda': '3811060.45', 'condona': False, 'financia': True}, 'cliente2': {'cod_cliente': 'CLT_002', 'valor_deuda': '2373749.89', 'condona': False, 'financia': True}}
{'cliente1': {'cod_cliente': 'CLT_003', 'valor_deuda': '3811060.45', 'condona': False, 'financia': True}, 'cliente2': {'cod_cliente': 'CLT_002', 'valor_deuda': '2373749.89', 'condona': False, 'financia': True}}


dict2 = dict(cliente1 = dict(cod_cliente = 'CLT_001', meses_adeuda = 5, acuerdo_pago = False,
             valores_deuda = dict(
                 deuda_mes_1 = dict(valor_deuda = 87654.57, tasa_interes = 4),
                 deuda_mes_2 = dict(valor_deuda = 9876543.57, tasa_interes = 20),
                 deuda_mes_3 = dict(valor_deuda = 154627.57, tasa_interes = 12),
                 deuda_mes_4 = dict(valor_deuda = 976430.57, tasa_interes = 20),
                 deuda_mes_5 = dict(valor_deuda = 1567893.57, tasa_interes = 35)
             )),
             cliente2 = dict(cod_cliente = 'CLT_002', meses_adeuda = 3, acuerdo_pago = False,
             valores_deuda = dict(
                 deuda_mes_1 = dict(valor_deuda = 87654.57, tasa_interes = 3),
                 deuda_mes_2 = dict(valor_deuda = 123456.98, tasa_interes = 8),
                 deuda_mes_3 = dict(valor_deuda = 345678.57, tasa_interes = 14)
             )),
             cliente3 = dict(cod_cliente = 'CLT_003', meses_adeuda = 5, acuerdo_pago = False,
             valores_deuda = dict(
                 deuda_mes_1 = dict(valor_deuda = 54367.57, tasa_interes = 5),
                 deuda_mes_2 = dict(valor_deuda = 123657.98, tasa_interes = 12),
                 deuda_mes_3 = dict(valor_deuda = 435678.34, tasa_interes = 15),
                 deuda_mes_4 = dict(valor_deuda = 745679.98, tasa_interes = 25),
                 deuda_mes_5 = dict(valor_deuda = 1435678.12, tasa_interes = 30)
             )),
            cliente4 = dict(cod_cliente = 'CLT_004', meses_adeuda = 2, acuerdo_pago = True,
             valores_deuda = dict(
                 deuda_mes_1 = dict(valor_deuda = 98765.57, tasa_interes = 3),
                 deuda_mes_2 = dict(valor_deuda = 167965.98, tasa_interes = 15)
             ))
             )


{'cliente1': {'cod_cliente': 'CLT_003', 'valor_deuda': '3495094.51', 'condona': False, 'financia': True}, 'cliente2': {'cod_cliente': 'CLT_002', 'valor_deuda': '617691.32', 'condona': True, 'financia': False}}


pp.pprint(evaluar_deuda(dict2))
