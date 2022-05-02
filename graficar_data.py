import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def conseguir_tamanos(data:pd.DataFrame, nom_col:str, labels=[]):
    tamanos = []
    total = np.shape(data)[0]
    for label in labels:
        valor = (np.shape(data[data[nom_col] == label ])[0]/total)*100
        tamanos.append(valor)
        
    return tamanos


def graficar_pie_plot(data:pd.DataFrame, nom_col:str, labels=[], explode=[] ):
    tamanos = conseguir_tamanos(data, nom_col, labels)
    
    
    fig1, ax1 = plt.subplots()
    ax1.pie(tamanos, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax1.axis('equal')
    
    plt.show()


def graficar_scatter_plot(data:pd.DataFrame, nom_col1:str, nom_col2:str, nom_col3:str,labels = [],
                          titulo='Sin titulo'):
    
    x=[]
    y=[]
    for label in labels:
        valorx = data[data[nom_col3] == label][nom_col1].apply('mean')
        valory = data[data[nom_col3] == label][nom_col2].apply('mean')
        
        x.append(valorx)
        y.append(valory)
        
    plt.scatter(x,y, c=[*range(0,len(x)*5,5)], cmap = 'viridis')
    plt.xlabel(nom_col1)
    plt.ylabel(nom_col2)
    plt.title(titulo)
    
    plt.colorbar()
    
    plt.show()
    
    
    
    
    
    