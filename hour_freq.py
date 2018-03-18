import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv
import time
import datetime

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

def count_hour(df, col):
    column = df[col]
    freq = {}
    flag = False
    for entry in column:
        if len(entry) > 15:
            cmp = entry[-8:-6]
            flag = True
        else:
            cmp = entry[-5:-3]

        if(cmp == ' 1'): print(entry, flag)
        if (cmp in freq):

            freq[str(cmp)] +=1
        else:
            freq[str(cmp)] = 1
    return freq


def readFiles(files_csv, func):
    '''Read multiple CSV files and apply the function
    '''
    for csv in files_csv:
        yield func(csv, 'Inicio_del_viaje')

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

files_csv = (pd.read_csv("2017/{0}".format(file_), encoding='latin-1', low_memory=False) for file_ in files)

total = sumDicts(readFiles(files_csv,count_hour))
pprint(total)
with open('output/horas.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in sorted(total.items(), key=operator.itemgetter(1))]
