import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv


destino=pd.read_csv("output/totalDestinoId.csv", encoding='latin-1').as_matrix()

origen=pd.read_csv("output/totalOrigenId.csv", encoding='latin-1').as_matrix()

total=pd.read_csv("output/totalAbs.csv", encoding='latin-1').as_matrix()

np_destino=np.array(destino[:,1])

np_origen=np.array(origen[:,1])

np_total=np.array(total[:,1])


plt.scatter(x=np_origen, y=np_destino, s=np_total/200)
plt.show()
