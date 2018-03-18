import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2)
df = pd.read_csv("modificados/nomenclatura_1.csv", encoding='latin-1').as_matrix()

coordenadas=np.array(df[:,3:5])
#model.fit(coordenadas)
latitud=np.array(coordenadas[:,0])
longitud=np.array(coordenadas[:,1])

total=pd.read_csv("modificados/totalTotal.csv", encoding='latin-1').as_matrix()

diferencia=np.array(total[:,5:7])
#print(diferencia)

"""o_d=np.array(total[:,1:3])
origen=np.array(total[:,1])
destino=np.array(total[:,2])"""
a=np.array(diferencia[:,0])
b=np.array(diferencia[:,1])

model.fit(diferencia)
labels=model.predict(diferencia)
#print(labels)
plt.xlabel("Diferencia de entradas y salidas")
plt.ylabel("Slots disponibles")
plt.title("")
plt.scatter(a,b, c=labels, alpha=0.5)
plt.show()
plt.ylabel("Latitud")
plt.xlabel("Longitud")
plt.title("Estacion por indicio de entradas y salidas")
plt.scatter(longitud,latitud, c=labels, alpha=0.5)
plt.show()

slot=np.array(diferencia[:,1])
slot=slot.reshape(-1,1)
model = KMeans(n_clusters=4)
model.fit(slot)
labels=model.predict(slot)
#print(labels)
plt.xlabel("Diferencia de entradas y salidas")
plt.ylabel("Slots disponibles")
plt.title("Clusters por numero de slots")
plt.scatter(a,b, c=labels, alpha=0.5)
plt.show()
plt.ylabel("Latitud")
plt.xlabel("Longitud")
plt.title("Slots por localizacion")
plt.scatter(longitud,latitud, c=labels, alpha=0.5)
plt.show()
