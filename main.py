import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cargar_data import conocer_tamano, listar_archivos_particulares
from conseguir_data import separar_por_tag, conseguir_tags, conseguir_tags2
from conseguir_data import conseguir_tags3, conseguir_tags4, conseguir_info_anime
from conseguir_data import conseguir_animes_por_var_numero, conseguir_elementos_unicos
from conseguir_data import conseguir_animes_por_var_cadena,conseguir_animes_por_palabra
from conseguir_data import conseguir_animes_por_filtro
from limpiar_data import limpiar_datos_float, limpiar_datos_int, limpiar_datos_object, limpieza_basica_datos
from modificar_data import modificar_dividir_columna, modificar_string_a_datetime 
from graficar_data import graficar_pie_plot, graficar_scatter_plot
from datetime import datetime
# animes = pd.read_csv("animes.csv")
# # print(conocer_tamano(datos)) || (18495, 17)
# animes = animes.dropna()
# # ruta = r"E:\JOHAN\retomando_python\oractica"
# # print(listar_archivos_particulares(ruta,"csv")) || ['Anime.csv']
# muestra = animes.sample(300)
# animes = modificar_dividir_columna(animes, " to ", 4, "release_year", "end_year")


# for index, row in animes.iterrows():
    
#     if row['release_year']=='Not available' or row['end_year']=='?':
#         animes=animes.drop(index)          
#         continue
    
#     if len(row['release_year'])==4:
#         nuevo_valor ='Jan 1, '+ row['release_year']
#         animes.loc[index,'release_year'] = nuevo_valor
        
#     elif len(row['release_year'])==9:      
#         fecha_split = row['release_year'].split(', ')
#         fecha_split.insert(1, ' 1, ')
#         animes.loc[index,'release_year']= ''.join(fecha_split)
        
        
#     if len(row['end_year'])==4:        
#         nuevo_valor ='Jan 1, '+ row['end_year']
#         animes.loc[index,'end_year'] = nuevo_valor
        
#     elif len(row['end_year'])==9:      
#         fecha_split = row['end_year'].split(', ')
#         fecha_split.insert(1, ' 1, ')
#         animes.loc[index,'end_year']= ''.join(fecha_split)
        
        
#     if (len(animes.loc[index,'end_year'])<11):
#         animes.loc[index, 'end_year'] = animes.loc[index, 'release_year']
        
#     animes.loc[index,'release_year'] = datetime.strptime(animes.loc[index,'release_year'], "%b %d, %Y").date()
#     animes.loc[index,'end_year'] = datetime.strptime(animes.loc[index,'end_year'], "%b %d, %Y").date()


animes = pd.read_csv('animes_procesado.csv')


import random

cantidad_de_animes_por_genero = animes['genre'].str.get_dummies("', '").sum()

colores=[]

for x in range(len(cantidad_de_animes_por_genero)):
    valor = random.random
    rgb = (valor(), valor(), valor())
    colores.append(rgb)

ordenado.plot(kind='barh', title="Cantidad de animes por género",
                                   xlabel = "Genero", grid=True, fontsize = 12,
                                   color=colores, figsize=(5,12))


# animes.sort_values(by='episodes', ascending=False).head(1).loc[:,['title'
# ,'episodes','release_year','end_year','members','score']]



# data = animes.describe(include="all")


# demon = conseguir_animes_por_palabra(animes,['title','score'],'synopsis','demon')

# conjunto_tags = conseguir_tags3(animes, "', '", 3, 2, 2,)

# conjunto_tags_repeticiones = conseguir_tags4(animes, "', '", 3,2,2)

# cantidad_de_anime_por_genero=pd.Series(conjunto_tags_repeticiones).value_counts()

# por_genero = animes['genre'].str.get_dummies("', '").sum()









# sample.iloc[:,i] = limpiar_datos_int(sample, sample.columns[i], -1)

# anime_hitori = conseguir_info_anime(datos, 'dangan')

#accion = separar_por_tag(sample, "Action")

# conjunto_tags = conseguir_tags(sample)

# conjunto_tags2 = conseguir_tags2(sample)

# veces_por_tag = pd.Series(conjunto_tags2).value_counts()

# anime_por_fecha = conseguir_animes_por_columna_int(sample, 'Release_year', 2020, 2022)

# anime_por_nombre = conseguir_animes_por_columna_string(sample, 'Name', 's')

# animes_por_pista = conseguir_animes_por_palabra_en_columna(sample,'Description','demon')

# anime_sexual = conseguir_animes_por_palabra_en_columna(datos,'Name', 'Hitori')

# animes = conseguir_animes_por_filtro(sample, release_year_inicio = 2020, release_season = 'spring')




#GRAFICOS
# graficar_pie_plot(datos, 'Release_season', labels=['Spring', 'Fall ', 'Winter', 'Summer'], explode = (0, 0.15, 0, 0.15) )
# =============================================================================
# 
# datos2 = datos[(datos['Episodes']>0) & (datos['Type'] == 'TV   ')]
# graficar_scatter_plot(datos2 ,'Rating', 'Episodes', 'Studio', list(np.unique(np.array(datos2['Studio']))), titulo="Animes: Episodios - Rating" )
# 
# =============================================================================






