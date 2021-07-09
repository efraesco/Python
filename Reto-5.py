import pandas as pd
#import os
#os.environ[ 'MPLCONFIGDIR' ] = '/tmp/'

def evaluar_csv(ruta_archivo: str):
    anyos = ['2012','2013','2014','2015','2016','2017','2018']
    #print(ruta_archivo.split("."))
    data_analitics = pd.read_csv(ruta_archivo, delimiter=',', encoding='UTF-8', na_values=['?'])
    #print(data_analitics)
    data_2012 = data_analitics['2012'].describe()
    data_2013 = data_analitics['2013'].describe()
    data_2014 = data_analitics['2014'].describe()
    data_2015 = data_analitics['2015'].describe()
    data_2016 = data_analitics['2016'].describe()
    data_2017 = data_analitics['2017'].describe()
    data_2018 = data_analitics['2018'].describe()
    data_25perc = [ data_2012['25%'],data_2013['25%'], data_2014['25%'], data_2015['25%'], data_2016['25%'], data_2017['25%'],data_2018['25%']]
    data_50perc = [ data_2012['50%'],data_2013['50%'], data_2014['50%'], data_2015['50%'], data_2016['50%'], data_2017['50%'],data_2018['50%']]
    data = {'Perceltiles 25 de Exportaciones':data_25perc, 'Perceltiles 75 de Exportaciones':data_50perc}
    data_percentil = pd.DataFrame(data, index=anyos)
    return data_percentil.to_dict()

url_archivo_csv = '/home/eescobarm/MINTIC2022/Programacion/retos-mintic-python/Exportaciones_De_Los_Principales_Renglones_Pecuarios.csv'
print(evaluar_csv(url_archivo_csv))


#python3 -m pip install -U pip
#python3 -m pip install -U matplotlib
#python3 -m pip install -U pandas


#{'Perceltiles 25 de Exportaciones': {'2012': 5262.5, '2013': 19382.5, '2014': 5257.0, '2015': 6345.5, '2016': 7251.0, '2017': 9519.0, '2018': 13420.5}, 'Perceltiles 75 de Exportaciones': {'2012': 295713.0, '2013': 155312.0, '2014': 43200.0, '2015': 85478.0, '2016': 87230.0, '2017': 83343.0, '2018': 61325.0}}
#{'Perceltiles 25 de Exportaciones': {'2012': 5262.5, '2013': 19382.5, '2014': 5257.0, '2015': 6345.5, '2016': 7251.0, '2017': 9519.0, '2018': 13420.5}, 'Perceltiles 75 de Exportaciones': {'2012': 295713.0, '2013': 155312.0, '2014': 43200.0, '2015': 85478.0, '2016': 87230.0, '2017': 83343.0, '2018': 61325.0}}

#***Error***
#Matplotlib created a temporary config/cache directory at /tmp/matplotlib-zxafxoje because the default path (/home/jobe00/.config/matplotlib) is not a writable directory; it is highly recommended to set the MPLCONFIGDIR environment variable to a writable directory, in particular to speed up the import of Matplotlib and to better support multiprocessing.