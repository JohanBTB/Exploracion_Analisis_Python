import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cargar_data import conocer_tamano, listar_archivos_particulares
from conseguir_data import separar_por_tag, conseguir_tags, conseguir_tags2, conseguir_info_anime
from conseguir_data import conseguir_animes_por_columna_int, conseguir_elementos_unicos
from conseguir_data import conseguir_animes_por_columna_string,conseguir_animes_por_palabra_en_columna
from conseguir_data import conseguir_animes_por_filtro
from limpiar_data import limpiar_datos_float, limpiar_datos_int, limpiar_datos_object, limpieza_basica_datos
from modificar_data import modificar_dividir_columna, modificar_string_a_datetime 
from graficar_data import graficar_pie_plot, graficar_scatter_plot
from datetime import datetime, date
animes = pd.read_csv("animes.csv")
# print(conocer_tamano(datos)) || (18495, 17)
animes = animes.dropna()
ruta = r"E:\JOHAN\retomando_python\oractica"
# print(listar_archivos_particulares(ruta,"csv")) || ['Anime.csv']
muestra = animes.sample(300)


muestra = modificar_dividir_columna(muestra, " to ", 4, "Release_year", "End_year")

for index, row in muestra.iterrows():
    
    if row['Release_year']=='Not available':
        muestra=muestra.drop(index)
    elif len(row['Release_year'])>9:
        pd.to_datetime(row['Release_year'], format='%b %d, %Y')
    elif len(row['Release_year'])==9:
        pd.to_datetime(' '.join(row['Release_year'].split().insert(1,' 01')), format='%b %d, %Y').date()
    else:
        pd.to_datetime('Jan 01, '+row['Release_year'] , format='%b %d, %Y')


# sample = datos.sample(300)

# for i in range(np.shape(sample)[1]):
#     if(sample.dtypes[i] == 'object'):
#         sample.iloc[:,i] = limpiar_datos_object(sample, sample.columns[i], "Unknown")

#     if(type(sample.dtypes[i])== 'int64'):
#         sample.iloc[:,i] = limpiar_datos_int(sample, sample.columns[i], -1)

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






