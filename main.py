import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cargar_data import conocer_tamano, listar_archivos_particulares
from conseguir_data import separar_por_tag, conseguir_tags, conseguir_tags2
from conseguir_data import conseguir_tags3, conseguir_tags4, conseguir_info_anime
from conseguir_data import conseguir_animes_por_var_numero, conseguir_elementos_unicos
from conseguir_data import conseguir_animes_por_var_cadena,conseguir_animes_por_palabra
from conseguir_data import conseguir_animes_por_filtro, conseguir_animes_por_genero
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


# =============================================================================
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
# =============================================================================


animes = pd.read_csv('animes_procesado.csv')


# import random

# cantidad_de_animes_por_genero = animes['genre'].str.get_dummies("', '").sum()

# colores=[]

# for x in range(len(cantidad_de_animes_por_genero)):
#     valor = random.random
#     rgb = (valor(), valor(), valor())
#     colores.append(rgb)

# cantidad_de_animes_por_genero.plot(kind='barh', title="Cantidad de animes por género",
#                                    xlabel = "Genero", grid=True, fontsize = 12,
#                                    color=colores, figsize=(5,12))


#Esta última linea fue para eliminar las cadenas que no tenian #ningún valor entre sus llaves


# =============================================================================
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# from PIL import Image
# import nltk
# # nltk.download('stopwords')
# 
# stopwords = nltk.corpus.stopwords.words('english')
# 
# archivo = open('stopwords.txt', "r")
# stopwords_propios = archivo.read().split()
# 
# imagen_fondo = np.array(Image.open('naruto.jpg'))
# imagen_colores = ImageColorGenerator(imagen_fondo)
# 
# texto = ''
# 
# for palabras in (animes['synopsis']):
#     texto = texto + palabras
#     
# word_cloud = WordCloud(stopwords = stopwords + stopwords_propios , collocations = False, width=1920, height=1080, 
#                         background_color = 'white',mask = imagen_fondo,  max_words = 500000).generate(texto)
# 
# word_cloud.recolor(color_func = imagen_colores)
# 
# plt.axis('off')
# plt.title('Palabras mas usadas')
# plt.imshow(word_cloud , interpolation = 'bilinear')
# 
# 
# 
# lista = WordCloud().process_text(texto)
# =============================================================================


# =============================================================================
# import matplotlib.pyplot as plt
# 
# temp_animes = animes.loc[:,['uid','release_year','episodes','members','popularity', 'score']].copy()
# temp_animes["agno"] = ""
# 
# lista = []
# for i in range(4):
#     fin = 2020-(i)*5
#     fin_fecha=pd.to_datetime(fin, format="%Y")
#     
#     inicio = 2020-((i+1)*5)
#     inicio_fecha = pd.to_datetime(inicio, format="%Y")
#     
#     lista.append(temp_animes[(pd.to_datetime(temp_animes['release_year'])>inicio_fecha) &
#                         (pd.to_datetime(temp_animes['release_year'])<=fin_fecha)])
#     
#     lista[i].agno = str(fin)+"-"+str(inicio)
# 
#    
# lista.append(temp_animes[pd.to_datetime(temp_animes['release_year'])<=pd.to_datetime(2000, format="%Y")])    
# 
# lista[4].agno = "1970>"
# 
# animes_por_fecha = pd.concat(lista)
# 
# 
# import seaborn as sns
# 
# 
# 
# fig, axs = plt.subplots(1,2, figsize = (15,5), dpi=600)
# sns.boxplot(x = 'popularity', y = "agno", data = animes_por_fecha,ax = axs[0])
# axs[0].title.set_text('Popularidad vs Agno')
# sns.boxplot(x = 'score', y = "agno", data = animes_por_fecha,ax = axs[1])
# axs[1].title.set_text('Score vs Agno')
# =============================================================================






# data = animes.describe(include="all")


# demon = conseguir_animes_por_palabra(animes,['title','score'],'synopsis','demon')

# conjunto_tags = conseguir_tags3(animes, "', '", 3, 2, 2,)

# conjunto_tags_repeticiones = conseguir_tags4(animes, "', '", 3,2,2)

# cantidad_de_anime_por_genero=pd.Series(conjunto_tags_repeticiones).value_counts()

# por_genero = animes['genre'].str.get_dummies("', '").sum()



# animes2 = conseguir_animes_por_genero(animes, "', '",'genre', ['score', 'popularity', 'genre2'])

# animes2['popularity'] = animes2['popularity'].astype(int)


# animes_agrupados = animes2.groupby(by=['genre2']).agg(['mean','median'])

# import seaborn as sns


# animes_mediana = animes2.groupby('genre2', as_index=False).median()



#========================    MEDIA     ===================================================================================

# animes_media = animes2.groupby('genre2', as_index=False).mean()
# fig, axs = plt.subplots(figsize=(8,12))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_media,
#                 hue_order = list(animes_media['genre2']), hue='genre2')

# for i in range(len(animes_media)):
#     fila = animes_media.loc[i, :]
#     plt.text(x=fila['score']+0.07,y=fila['popularity'],s=fila['genre2'], 
#              fontdict=dict(color='red',size=10))




# fig, axs = plt.subplots(figsize=(12,13))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_media,
#                 hue_order = list(animes_media['genre2']), hue='genre2')

# for i in range(len(animes_media)):
    
#     fila = animes_media.loc[i, :]
#     if fila['score']<6.5:
#         continue
#     plt.text(x=fila['score']+0.01,y=fila['popularity'],s=fila['genre2'], 
#              fontdict=dict(color='red',size=10))

# plt.xlim((6.5,7.3))




#========================    MEDIANA     ====================================================

# fig, axs = plt.subplots(figsize=(8,12))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_mediana,
#                 hue_order = list(animes_mediana['genre2']), hue='genre2')

# for i in range(len(animes_mediana)):
#     fila = animes_mediana.loc[i, :]
#     plt.text(x=fila['score']+0.07,y=fila['popularity'],s=fila['genre2'], 
#              fontdict=dict(color='red',size=10))




# fig, axs = plt.subplots(figsize=(12,13))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_mediana,
#                 hue_order = list(animes_mediana['genre2']), hue='genre2')

# for i in range(len(animes_mediana)):
    
#     fila = animes_mediana.loc[i, :]
#     if fila['score']<6.5:
#         continue
#     plt.text(x=fila['score']+0.01,y=fila['popularity'],s=fila['genre2'], 
#              fontdict=dict(color='red',size=10))

# plt.xlim((6.5,7.8))


import matplotlib.pyplot as plt

temp_animes = animes.loc[:,['uid','release_year','members','popularity', 'score']].copy()
temp_animes["agno"] = ""

lista = []
for i in range(4):
    fin = 2020-(i)*5
    fin_fecha=pd.to_datetime(fin, format="%Y")
    
    inicio = 2020-((i+1)*5)
    inicio_fecha = pd.to_datetime(inicio, format="%Y")
    
    lista.append(temp_animes[(pd.to_datetime(temp_animes['release_year'])>inicio_fecha) &
                        (pd.to_datetime(temp_animes['release_year'])<=fin_fecha)])
    
    lista[i].agno = str(fin)+"-"+str(inicio)
    
lista.append(temp_animes[pd.to_datetime(temp_animes['release_year'])<=pd.to_datetime(2000, format="%Y")])    
lista[4].agno = "1970>"

animes_por_fecha = pd.concat(lista)

animes_agrupados = animes_por_fecha.groupby(by='agno').count()
 

animes_agrupados.plot( kind = 'pie', x='agno', y = 'uid',legend = True, ylabel = '',
                      title = 'Animes emitidos  por años', colormap = plt.get_cmap('cool'),
                      figsize=(10,13), shadow = True, autopct = "%1.1f%%", fontsize=12)

plt.legend(loc='upper left')

















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






