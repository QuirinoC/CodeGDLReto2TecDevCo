import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
genero = {}
#dec = pd.read_csv('2017/datos_abiertos_2017_12.csv', chunksize=10, encoding='latin-1')
jan = pd.read_csv('2017/datos_abiertos_2017_01.csv', encoding='latin-1')
#print(next(jan['Genero']))
print(jan['Genero'])
col_genero = jan['Genero']
for entry in col_genero:
    if (entry in genero):
        genero[entry] += 1
    else:
        genero[entry] = 1

print(genero)

def ejemplo():
    pass
