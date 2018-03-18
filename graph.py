import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv
np.random.seed(1632369)

destino=pd.read_csv("output/totalDestinoId.csv", encoding='latin-1').as_matrix()

origen=pd.read_csv("output/totalOrigenId.csv", encoding='latin-1').as_matrix()

total=pd.read_csv("output/totalAbs.csv", encoding='latin-1').as_matrix()

np_destino=np.array(destino[:,1])

np_origen=np.array(origen[:,1])

np_total=np.array(total[:,1])

etiquetas = pd.read_csv("nomenclatura_1.csv", encoding='latin-1').as_matrix()
colors = np.random.rand(238)

plt.xlabel('Total de salidas')
plt.ylabel('Total de llegadas')

plt.grid(True)

plt.text(49400, 60000, 'GDL - 049', ha='center',va='center')
plt.text(46700, 50000, 'GDL - 048', ha='center',va='center')
plt.text(42000, 43000, 'GDL - 050', ha='center',va='center')
plt.text(43000, 35000, 'GDL - 009', ha='right',va='center')
plt.text(38000, 31500, 'GDL - 073', ha='center',va='center')
plt.text(35000, 37500, 'GDL - 052', ha='center',va='center')
plt.text(28000, 39000, 'GDL - 054', ha='center',va='center')

plt.text(80, 45000, " GDL - 049 Lopez Cotilla/ Marcos Castellanos \n \
GDL - 048 C. Escorza / Av. Vallarta \n \
GDL - 050 C. Pedro Moreno / Calz. Federalismo \n \
GDL - 009 Calz. Federalismo/ C. J. Angulo \n \
GDL - 073 Av. La Paz / Av. Federalismo \n \
GDL - 052 Av. Juarez / Av. 16 de Septiembre \n \
GDL - 054 Av. Juarez / Calz. Independencia", size=8)

labels = np.array(etiquetas[:,1])
print(labels)
new_labels = []
for label, value in zip(labels, total[:,1]):
    if (int(value) < 60000):
        new_labels.append('')
    else:
        new_labels.append('')


labels = np.array(new_labels)

print(labels)
'''
#CodeGDL
#MLHLocalHost
'''
for label, x, y in zip(labels, np_origen, np_destino):
    plt.annotate(
        label,
        xy=(x, y), xytext=(0, 0),
        textcoords='offset points', ha='center', va='center',
        #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),

        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))


plt.title("Total de viajes por estación(2017)")
plt.scatter(x=np_origen, y=np_destino, s=np_total/100, c=colors,  alpha=0.5)
plt.show()
