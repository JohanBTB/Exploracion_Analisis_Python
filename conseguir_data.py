import pandas as pd
import numpy as np
from cargar_data import conseguir_posicion_columna



def separar_por_tag(data:pd.DataFrame , name_tag:str, num_col_buscar:int):
    tabla_por_tag = pd.DataFrame()
    
    for i in range(np.shape(data)[0]):
        tags = data.iloc[i,num_col_buscar].split(sep = ", ")
        
        for tag in tags:
           
            if(name_tag == tag):
                             
                
                tabla_por_tag = tabla_por_tag.append(dict(data.iloc[i, :]), ignore_index = True)
    return tabla_por_tag
#Devuelve un dataframe separado por el tag establecido como argumento

def conseguir_tags(data:pd.DataFrame, num_col_buscar:int):
    conjunto_tags = {"ejemplo"}
    
    for i in range(len(data)):
        tags = data.iloc[i,num_col_buscar].split(sep = ", ")
        for tag in tags:
            conjunto_tags.add(tag)
    conjunto_tags.remove('ejemplo')
    return list(conjunto_tags)
#Esta funcion devuelve una lsita de todos los tags que hay en la tabla(no se
#repiten)
#Busca en columnas que tengan sus valores separados por coma
def conseguir_tags2(data:pd.DataFrame, num_col_buscar:int):
    conjunto_tags = []
    for i in range(len(data)):
        tags = data.iloc[i,num_col_buscar].split(sep = ',')
        for tag in tags:
            conjunto_tags.append(tag)
    return conjunto_tags
#Esta funcion devuelve una lista que incluye todos los tags de la tabla(se 
#pueden repetir)

#Busca en columnas que tengan sus valores separados por coma


def conseguir_tags3(data:pd.DataFrame, sep:str, num_col_buscar,inicio:int,fin:int):
    conjunto_tags = {''}
    
    for i in range(len(data)):
        tags = data.iloc[i,num_col_buscar][inicio:len(data.iloc[i,num_col_buscar])-fin].split(sep = sep)
        for tag in tags:
            conjunto_tags.add(tag)
    conjunto_tags.remove('')
    return list(conjunto_tags)
#Esta funcion devuelve una lsita de todos los tags que hay en la tabla(no se
#repiten)

#Busca en columnas que tengan sus valores separados por un valor, pero con un
#inicio y fin determinados

def conseguir_tags4(data:pd.DataFrame, sep:str, num_col_buscar, inicio:int, fin:int):
    conjunto_tags = []
    for i in range(len(data)):
        tags = data.iloc[i,num_col_buscar][inicio:len(data.iloc[i,num_col_buscar])-fin].split(sep = sep)
        for tag in tags:
            conjunto_tags.append(tag)
    return conjunto_tags

#Esta funcion devuelve una lista que incluye todos los tags de la tabla(se 
#pueden repetir)

#Busca en columnas que tengan sus valores separados por un valor, pero con un
#inicio y fin determinados.





# ==============================================================================================================================================

#METODOS QUE DEVUELVEN TODA LA FILA SEGUN EL VALOR INGRESADO

def conseguir_info_anime(data:pd.DataFrame, pista:str):
    animes = pd.DataFrame(data =None, columns = data.columns)
    pista = pista.lower()
    for index, anime in data.iterrows():
        if(anime['title'].lower().find(pista) != -1):
            animes = animes.append(anime, ignore_index = True)
    
    return animes
#Devuelve toda la fila de los animes segun la pista


def conseguir_animes_por_genero(data:pd.DataFrame, sep:str, nom_col_buscar, nom_col_devolver):
    data[nom_col_devolver[-1]] = ''
    data2 = pd.DataFrame(columns = nom_col_devolver)

    for i in range(len(data)):
        tags = data.loc[i, nom_col_buscar].split(sep = sep)
        for tag in tags:
            fila = data.loc[i, nom_col_devolver]
            fila[nom_col_devolver[-1]] = tag
            data2=data2.append(fila, ignore_index = True)

            
    return data2



# ==============================================================================================================================================


#METODOS QUE DEVUELVEN COLUMNAS DETERMINADAS DE LA TABLA SEGUN EL VALOR INGRESADO

def conseguir_elementos_unicos(data:pd.DataFrame, num_col:int):
    return data.iloc[:,num_col].unique()
#Devuelve los elementos unicos de una columna de una tabla

def conseguir_animes_por_var_numero(data:pd.DataFrame, nom_col:str,inicio:int, fin:int):
    # por_fecha=pd.DataFrame(columns = data.columns)
    animes_por_int = data[(data[nom_col] >= inicio) & (data[nom_col] <= fin)]
    return animes_por_int
#Devuelve el nombre de los animes que se encuentran entre dos ints

def conseguir_animes_por_var_cadena(data:pd.DataFrame, nom_col:str, pista:str):
    pista = pista.lower()
    len_pista = len(pista)
    num_col = conseguir_posicion_columna(data, nom_col)
    animes_por_string = []
    if num_col != -1:
        animes_por_string = [anime for anime in data.iloc[:, num_col] if anime[0:len_pista].lower() == pista]
    return animes_por_string
#Devuelve los datos de la tabla de una columna que comience con la pista


def conseguir_animes_por_palabra(data: pd.DataFrame, nom_col_devolver,nom_col_buscar:str, pista:str):
    pista = pista.lower()
    num_col = conseguir_posicion_columna(data, nom_col_buscar)
    
    nom_animes = []
    
    if(num_col != -1):
        print("Se encontraron titulos de anime")
        for index, row in data.iterrows():
            if(row[nom_col_buscar].lower().find(pista) != -1):
               nom_animes.append(row[nom_col_devolver])
    else:
        print("No se encontro la columna en donde buscar")    
        
    return pd.DataFrame(nom_animes)

#Devuelve los animes que tengan la pista dentro del contenido de la columna


def conseguir_animes_por_lista(data: pd.DataFrame, nom_col_devolver:list,nom_col_buscar, pista:str):
    pista = pista.lower()
    num_col = conseguir_posicion_columna(data, nom_col_buscar)
    
    nom_animes = []
    
    if(num_col != -1):
        print("Se encontraron titulos de anime")
        for index, row in data.iterrows():
            if(row[nom_col_buscar].lower().find(pista) != -1):
               nom_animes.append(row[nom_col_devolver])
    else:
        print("No se encontro la columna en donde buscar")    
        
    return pd.DataFrame(nom_animes)
#Devuelve las columnas de los animes que tienen en cierta variable el valor
# de la pista

# ==============================================================================================================================================


def conseguir_animes_por_filtro(data: pd.DataFrame, rank_inicio = 0, rank_fin = 20000, name = '',
                               japanese_name = '', type_name = '', episodios_inicio = 0,
                               episodios_fin = 10000, studio = '', release_season = '', tags = [],
                               rating_inicio= 0, rating_fin = 5, release_year_inicio = 1000,
                               release_year_fin = 3000, content_warning = [], related_mange = '',
                               related_anime = ''):
    
    resultado = pd.DataFrame(data = None, columns = data.columns)

    if(name or japanese_name or type_name or studio or release_season or related_mange or related_anime or content_warning or tags):
        for index, row in data.iterrows():
            if name:
                if(row['Name'].lower().find(name) != -1):
                    resultado = resultado.append(row)
                    continue
            
            if japanese_name:
                if(row['Japanese_name'].lower().find(japanese_name) != -1):
                    resultado = resultado.append(row)
                    continue    
                
            
            if type_name:
                if(row['Type'].lower().find(type_name) != -1):
                    resultado = resultado.append(row)
                    continue   
            
            if studio:
                if(row['Studio'].lower().find(studio) != -1):
                    resultado = resultado.append(row)
                    continue   
                
            if release_season:
                if(row['Release_season'].lower().find(release_season) != -1):
                    resultado = resultado.append(row)
                    continue
            
            if related_mange:
                if(row['Related_Mange'].lower().find(related_mange) != -1):
                    resultado = resultado.append(row)
                    continue
                
            if related_anime:  
                if(row['Related_anime'].lower().find(related_anime) != -1):
                    resultado = resultado.append(row)
                    continue
            
            if content_warning:
                valor = True
                for content in content_warning:
                    if(row['Content_Warning'].lower().find(content) == -1):
                        valor = False
                        break
                
                if(valor):
                    resultado = resultado.append(row)
                    
                continue
            
            
            valor = True
            for tag in tags:
                if(row['Tags'].lower().find(tag) == -1):
                    valor = False
                    
                    break
                
                if(valor):
                    resultado = resultado.append(row)
            
    else:
        resultado = data
    
    if(rank_inicio >0):
        resultado = resultado[resultado['Rank'] > rank_inicio]
    if(rank_fin < 20000):
        resultado = resultado[resultado['Rank'] < rank_fin]
    
    
    if(episodios_inicio>0):
        resultado = resultado[resultado['Episodes'] >= episodios_inicio]
    if(episodios_fin<10000):
        resultado = resultado[resultado['Episodes'] <= episodios_fin]


    if(rating_inicio>0):
        resultado = resultado[resultado['Rating'] > rating_inicio]
    if(rating_fin<5):
        resultado = resultado[resultado['Rating'] < rating_fin]
    
    
    if(release_year_inicio>0):
        resultado = resultado[resultado['Release_year'] > release_year_inicio]
    if(release_year_fin<5):
        resultado = resultado[resultado['Release_year'] < release_year_fin]
    
    
    
    
#Devuelve las filas de la tabla que cumplen con los filtros    
    
    
    
    return resultado


