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



# =============================================================================
# import seaborn as sns
# 
# conteo_por_genero = pd.DataFrame(conseguir_tags2(animes, 3, "', '"), columns = ['genre']).sort_values('genre')
# 
# colores = sns.color_palette("flare")
# 
# plt.figure(figsize=(10,12))
# 
# sns.countplot(data = conteo_por_genero,y = 'genre', hue_order='genre' ,palette =colores )
# 
# =============================================================================

# =================================Word Cloud==================================
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

from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns


temp_animes = animes.loc[:,['uid','release_year','episodes','members','popularity', 'score']]
temp_animes = temp_animes.astype({'release_year':'datetime64'})

temp_animes_agrupados = temp_animes[temp_animes['release_year'] < datetime(year=2000,month=1,day=1)]
temp_animes.drop(temp_animes_agrupados.index, inplace=True)

temp_animes_agrupados["release_year"]="<2000"

for i in range(4):
    fin = datetime(year=2005 + i*5, month=1,day=1)
    
    temp = temp_animes[temp_animes['release_year'] <= fin]
    temp['release_year'] = "{}-{}".format(fin.year-5,fin.year)
    temp_animes.drop(temp.index, inplace = True)
    temp_animes_agrupados = pd.concat([temp_animes_agrupados, temp])
    



fig, axs = plt.subplots(1,2, figsize = (15,8), dpi=200)
sns.boxplot(x = 'members', y = "release_year", data = temp_animes_agrupados,ax = axs[0])
axs[0].title.set_text('Miembros vs Tiempo')
sns.boxplot(x = 'episodes', y = "release_year", data = temp_animes_agrupados,ax = axs[1])
axs[1].title.set_text('Episodios vs Tiempo')


#===================================Scatterplot===================================



# temp_animes = animes.loc[:, ['uid', 'score', 'popularity', 'genre']]
# temp_animes['genre'] = temp_animes['genre'].str.split("', '")
# temp_animes = temp_animes.explode('genre')



#========================    MEDIA     ===================================================================================

# animes_agrupados = temp_animes.groupby('genre', as_index = False).agg(['mean','median'])


# animes_media = temp_animes.groupby('genre', as_index=False).mean()

# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, axs = plt.subplots(figsize=(8,12))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_media,
#                 hue_order = list(animes_media['genre']), hue='genre')

# for i in range(len(animes_media)):
#     fila = animes_media.loc[i, :]
#     plt.text(x=fila['score']+0.07,y=fila['popularity'],s=fila['genre'], 
#               fontdict=dict(color='red',size=10))




# fig, axs = plt.subplots(figsize=(12,13))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_media,
#                 hue_order = list(animes_media['genre']), hue='genre')

# for i in range(len(animes_media)):
    
#     fila = animes_media.loc[i, :]
#     if fila['score']<6.5:
#         continue
#     plt.text(x=fila['score']+0.01,y=fila['popularity'],s=fila['genre'], 
#               fontdict=dict(color='red',size=10))

# plt.xlim((6.5,7.3))
# plt.ylim((2000,9000))



#========================    MEDIANA     ====================================================

# animes_mediana = temp_animes.groupby('genre', as_index =False).median()

# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, axs = plt.subplots(figsize=(8,12))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_mediana,
#                 hue_order = list(animes_mediana['genre']), hue='genre')

# for i in range(len(animes_mediana)):
#     fila = animes_mediana.loc[i, :]
#     plt.text(x=fila['score']+0.07,y=fila['popularity'],s=fila['genre'], 
#               fontdict=dict(color='red',size=10))




# fig, axs = plt.subplots(figsize=(12,13))

# axs = sns.scatterplot(x = 'score', y = 'popularity', data = animes_mediana,
#                 hue_order = list(animes_mediana['genre']), hue='genre')

# for i in range(len(animes_mediana)):
    
#     fila = animes_mediana.loc[i, :]
#     if fila['score']<6.5:
#         continue
#     plt.text(x=fila['score']+0.01,y=fila['popularity'],s=fila['genre'], 
#               fontdict=dict(color='red',size=10))

# plt.xlim((6.5,7.6))
# plt.ylim(1500,9000)

# ==================================Pie plot===================================
# from datetime import date
# import matplotlib.pyplot as plt

# temp_animes = animes.loc[:,['uid','release_year','episodes','members','popularity', 'score']]
# temp_animes = temp_animes.astype({'release_year':'datetime64'})

# temp_animes_2000 = temp_animes[temp_animes['release_year'] < datetime(year=2000,month=1,day=1)]
# temp_animes.drop(temp_animes_2000.index, inplace=True)

# temp_animes_2000["release_year"]="<2000"
# temp_animes_2000 = temp_animes_2000.groupby('release_year', as_index = True).count()
# temp_animes = temp_animes.groupby([pd.Grouper(key = 'release_year', freq = "5Ys",
#                                               closed = "left", origin = "2000-01-01")]).count()
# temp_animes.index = [x.strftime("%Y")+ "-" + str(x.year+5) for x in temp_animes.index]
# temp_animes = pd.concat([temp_animes_2000, temp_animes])


  

# temp_animes.plot( kind = 'pie', x='release_year', y = 'uid',legend = True, ylabel = '',
#                  xlabel = temp_animes['popularity'], title = 'Animes emitidos  por periodos de años',
#                  colormap = plt.get_cmap('cool'), figsize=(10,13), shadow = True, autopct = "%1.1f%%",
#                  fontsize=12)

# plt.legend(loc='right')
# 
# 
# =============================================================================

# =======================Barplot==============================================

# animes_temp = animes.loc[:,['uid','title','genre','score']]
# animes_temp['genre'] = animes['genre'].str.split("', '")
# animes_temp = animes_temp.explode('genre')

# animes_conteo = animes_temp.groupby(by='genre', as_index=False).count()
# animes_conteo.rename(columns = {'score':'quantity'}, inplace =True)
# animes_conteo.sort_values(by='quantity', inplace=True, ascending=False)
# top_animes_por_cantidad = animes_conteo['genre'][:10]


#---------------------------Puede ser asi-------------------------------------

# animes_temp.drop_duplicates(subset = 'uid', inplace = True)

# generos_max_min = pd.DataFrame(columns = animes_temp.columns)
# for genero in top_animes_por_cantidad:
#     genero_df = animes_temp[animes_temp['genre'] == genero].sort_values('score', ascending = False)
    
#     genero_max = genero_df.iloc[0,:]
#     genero_max['valor'] = 'maximum'
    
#     genero_min = genero_df.iloc[-1,:]
#     genero_min['valor'] = 'minimum'
    
#     generos_max_min = generos_max_min.append(genero_max).append(genero_min)


# -----------------------------Puede ser asi ---------------------------------
# generos_max_min = pd.DataFrame(columns = animes_temp.columns)
# for genero in top_animes_por_cantidad:
#     genero_df = animes_temp[animes_temp['genre'] == genero]
    
#     genero_max = animes_temp.loc[genero_df['score'].idxmax()]
#     genero_max['valor'] = 'maximum'
    
#     genero_min = animes_temp.loc[genero_df['score'].idxmin()]
#     genero_min['valor'] = 'minimum'
    
#     generos_max_min = generos_max_min.append(genero_max).append(genero_min)

# import seaborn as sns
# import matplotlib.pyplot as plt

# plt.figure(figsize=(11,9))
# sns.barplot(x = 'genre', y = 'score', hue = 'valor', data = generos_max_min)
# for i in range(len(generos_max_min)):
#     fila = generos_max_min.iloc[i, :]
#     score = fila['score']
#     titulo = fila['title'] if len(fila['title'])<10 else fila['title'][:15]+"..."
    
#     if i%2==0:
#         plt.text(x=i/2-0.3 ,y=(score/2)-2, s = titulo, 
#               fontdict=dict(color='white',size=15), rotation = 90)
    
#     else:
#         plt.text(x=(i/2)-0.35 ,y=(score/2)-1, s = titulo, 
#               fontdict=dict(color='white',size=15), rotation = 90)


# 
# =============================================================================

# =============================================================================
# import seaborn as sns
# import matplotlib.pyplot as plt
# from datetime import date
# 
# temp_animes = animes.loc[:, ['uid','release_year','score','genre']]
# temp_animes['genre'] = temp_animes['genre'].str.split("', '")
# temp_animes = temp_animes.explode('genre')
# temp_animes = temp_animes.astype({'release_year':'datetime64'})
# 
# temp_animes = temp_animes[temp_animes['release_year'] > datetime(year=2000,month=1,day=1)]
# temp_animes = temp_animes.groupby([pd.Grouper(key = 'release_year', freq = "2Y"), 'genre']).agg({'score':'mean'}).reset_index()
# temp_animes['release_year'] = temp_animes['release_year'].dt.strftime('%Y')
# 
# 
# temp_animes_pivot = temp_animes.pivot(index = 'genre', columns = 'release_year', values = 'score')
# 
# 
# 
# plt.figure(figsize=(12,9))
# 
# sns.heatmap(temp_animes_pivot, cmap="BuRd", center = temp_animes['score'].mean(), annot = True)
# 
# 
# =============================================================================




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