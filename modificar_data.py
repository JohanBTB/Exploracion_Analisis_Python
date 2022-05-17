import pandas as pd
import numpy as np


def modificar_dividir_columna(datos:pd.DataFrame,cadena_separadora, col_fecha:int,nom_col1:str, nom_col2:str):
    
    fecha_columnas = [x.split(" to ") for x in datos.iloc[:,col_fecha]]
    
    for fila in fecha_columnas:
        if(len(fila)==1):
            fila.append(fila[0])
            
    datos =datos.drop(datos.columns[col_fecha], axis=1)
    datos.insert(loc=col_fecha, column = nom_col1, value = [x[0] for x in fecha_columnas])
    datos.insert(loc=col_fecha+1, column = nom_col2, value = [x[1] for x in fecha_columnas])
    
    return datos

