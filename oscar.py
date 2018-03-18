import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv

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

files = ["datos_abiertos_2017_0{0}.csv".format(x) for x in range(1,10)] + \
        ["datos_abiertos_2017_{0}.csv".format(x) for x in range(10,13)]

files_csv = (pd.read_csv("2017/{0}".format(file), encoding='latin-1', low_memory=False) for file in files)

months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',\
          'Septiembre','Octubre','Noviembre','Diciembre',]

def generateFiles():
    counter = 0
    for csv_file in files_csv:
        total = count_freq(csv_file, 'Origen_Id')
        total = sumDicts([count_freq(csv_file, 'Origen_Id'),count_freq(csv_file, 'Destino_Id')])
        with open('outputMonth/{0}.csv'.format(months[counter]), 'w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in sorted(total.items(), key=operator.itemgetter(1))]
        counter += 1

df_ = pd.DataFrame()
df_ = df_.fillna(0) # with 0s rather than NaNs
df_['Estacion'] = pd.read_csv("outputMonth/Enero.csv", encoding='latin-1', low_memory=False)['Estacion']
for i in range(12):
    df_[months[i]] = pd.read_csv("outputMonth/{0}.csv".format(months[i]), encoding='latin-1', low_memory=False)['Viajes']

df_.to_csv("outputMonth/freq_month.csv")
