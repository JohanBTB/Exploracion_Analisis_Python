import pandas as pd
import numpy as np

def conseguir_tags2(data:pd.DataFrame, num_col_buscar:int, sep:str):
    conjunto_tags = []
    for i in range(len(data)):
        tags = data.iloc[i,num_col_buscar].split(sep = sep)
        for tag in tags:
            conjunto_tags.append(tag)
    return conjunto_tags



