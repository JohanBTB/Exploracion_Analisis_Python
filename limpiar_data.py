import pandas as pd
import numpy as np



def limpiar_datos_int(datos:pd.DataFrame, columna:str, valor=0):
    return datos[columna].fillna(valor)
#Convierte los datos nan de una columna tipo int en 0
    
def limpiar_datos_object(datos:pd.DataFrame, columna:str, valor="Unknown"):
    return datos[columna].fillna(valor)
#Convierte los datos nan de una columna tipo object en "Unknown"    

def limpiar_datos_float(datos:pd.DataFrame, columna:str, valor = 0):
    return datos[columna].fillna(valor)
#Convierte los datos nan de una columna tipo float en 0


def limpieza_basica_datos(data:pd.DataFrame, reemplazo_null_str, reemplazo_null_int):
    for i in range(np.shape(data)[1]):
        if(data.dtypes[i] == 'object'):
            data.iloc[:,i] = limpiar_datos_object(data, data.columns[i], reemplazo_null_str)
    
        if(type(data.dtypes[i])== 'int64' ):
            data.iloc[:,i] = limpiar_datos_int(data, data.columns[i], reemplazo_null_int)

    return 

