import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv

counter = 0
def count_freq(df, col):
    column = df[col]
    freq = {}
    for entry in column:
        if(entry in freq):
            freq[entry] +=1
        else:
            freq[entry] = 1
    return freq

def readFiles(files_csv, func):
    '''Read multiple CSV files and apply the function
    '''
    for csv in files_csv:
        yield func(csv, 'Destino_Id')

def sumDicts(dicts):
    '''Takes multiple dictionaries and returns a sum in another dict
    '''
    total = {}
    for result in dicts:
        for key, value in result.items():
            if key in total:
                total[key] += value
            else:
                total[key] = value
    return total

#Create a list with the name of the files
files = ["datos_abiertos_2017_0{0}.csv".format(x) for x in range(1,10)] + \
        ["datos_abiertos_2017_{0}.csv".format(x) for x in range(10,13)]

#Create a generator of pandas DataFrames
files_csv = (pd.read_csv("2017/{0}".format(file), encoding='latin-1', low_memory=False) for file in files)
#Importante
#total = sumDicts(readFiles(files_csv, count_freq))

#with open('output/totalDestinoId.csv', 'w') as f:
#    [f.write('{0},{1}\n'.format(key, value)) for key, value in sorted(total.items(), key=operator.itemgetter(1))]

#pprint(total)

nomenclatura = (open("nomenclatura_1.csv", "r"))
nomenclatura =nomenclatura.read().split('\n')
nomenclatura = nomenclatura[:-1]
estaciones = []
length = len(nomenclatura)
for line in nomenclatura:
    cols = line.split(',')
    estaciones.append([cols[0],cols[3],cols[4]])
print(estaciones)





print("Done.")
