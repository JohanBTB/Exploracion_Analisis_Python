from zipfile import ZipFile
import pandas as pd
import numpy as np
import os


def conseguir_posicion_columna(data:pd.DataFrame, nom_col:str):
    num_col = -1
    for i in range(len(data.columns)):
        
        if(data.columns[i]==nom_col):
            num_col = i
            i = len(data.columns)
            pass
    return num_col

def extra_archivos(nombre_archivo):
    
    with ZipFile(nombre_archivo, "r") as zipped:
        zipped.extractall()
#Extrae archivos de una carpeta zip

def conocer_tamano(data:pd.DataFrame):
    return (np.shape(data))
#Devuelve el tamano de un dataframe

def listar_archivos_particulares(ruta:str, sufijo:str):
    archivos_particulares = []
    
    archivos = os.listdir(ruta)
    
    for archivo in archivos:
        if(os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith(sufijo)):
            archivos_particulares.append(archivo)
            
    return archivos_particulares
#Devuelve una lista de archivos con cierto sufijo