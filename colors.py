import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv
np.random.seed(1632369)



destino_ = pd.read_csv("output/totalDestinoId.csv", encoding='latin-1')
destino=destino_.as_matrix()

origen_= pd.read_csv("output/totalOrigenId.csv", encoding='latin-1')
origen=origen_.as_matrix()

total_=pd.read_csv("output/totalAbs.csv", encoding='latin-1')
total=total_.as_matrix()

np_destino=np.array(destino[:,1])

np_origen=np.array(origen[:,1])

np_total=np.array(total[:,1])

etiquetas_= pd.read_csv("nomenclatura_1.csv", encoding='latin-1')
etiquetas = etiquetas_.as_matrix()
#colors = np.random.rand(238)

'''
UDG latitude, longitude
min 20.63613, -103.33357
max 20.66468, -103.301239
point(max - point >0 min)

Zapopan-Centro
Vertical
ZPN-001	20.73244
ZPN-013	20.720438
Horizontal
ZPN-030	-103.399976
ZPN-024	-103.381901

Guadalajara-Centro
    latitude longitude
min 20.6625, -103.38488
max 20.69865,-103.33343

Vallarta
Vertical
ZPN-031	20.67342
GDL-158	20.65158
Horizontal
ZPN-034	-103.40968
GDL-155	-103.38838

20.6641,-103.4003,11
'''
def map_color(x,y):
    '''Map value to a color'''
    colors = []
    for i in x:
        if (i >= -103.33357 and i <= -103.301239):
            #UDG
            colors.append('red')
        elif (i >= -103.399976 and i <= -103.381901):
            #Zapopan-Centro
            colors.append('black')
        elif (i >= -103.38488 and i <= -103.33343):
            #Guadalajara-Centro
            colors.append('blue')
        elif (i >= -103.40968 and i <= -103.38838):
            colors.append('yellow')
        else: colors.append('black')
    counter = 0
    for i in y:
        if   (i >= 20.63613 and i <= 20.66468): colors[counter] = 'red'
        elif (i >= 20.720438 and i <= 20.73244): colors[counter] = 'black'
        elif (i >= 20.6625 and i <= 20.69865): colors[counter] = 'blue'
        elif (i >= 20.65158 and i <= 20.67342): colors[counter] = 'yellow'
        else: colors[counter] = 'black'
    return np.array(colors)

    '''
    print(x)
    if ():
        return 'red'
    else:
        return 'black'
    '''
x = etiquetas_['longitude']
y = etiquetas_['latitude']

colors = map_color(x,y)

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




#Labels mayores
plt.text(-2600, 46000, " GDL - 049 Lopez Cotilla/ Marcos Castellanos \n \
GDL - 048 C. Escorza / Av. Vallarta \n \
GDL - 050 C. Pedro Moreno / Calz. Federalismo \n \
GDL - 009 Calz. Federalismo/ C. J. Angulo \n \
GDL - 073 Av. La Paz / Av. Federalismo \n \
GDL - 052 Av. Juarez / Av. 16 de Septiembre \n \
GDL - 054 Av. Juarez / Calz. Independencia", size=12)

#Labels colores
plt.text(-2000, 30000, "UDG - Rojo\nZapopan_Centro - Negro\nGuadalajara-Centro - Azul\nYellow")

labels = np.array(etiquetas[:,1])
#Aqui

new_labels = []
for label, value in zip(labels, total[:,1]):
    if (int(value) < 60000):
        new_labels.append('')
    else:
        new_labels.append('')


labels = np.array(new_labels)



'''
#CodeGDL
#MLHLocalHost
'''
range_latitude  = etiquetas_['latitude'].max() - etiquetas_['latitude'].min()
range_longitude = etiquetas_['longitude'].max() - etiquetas_['longitude'].min()





for label, x, y in zip(labels, np_origen, np_destino):
    plt.annotate(
        label,
        xy=(x, y), xytext=(0, 0),
        textcoords='offset points', ha='center', va='center',
        #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),

        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))


plt.title("Total de viajes por estación(2017)")
plt.scatter(x=np_origen, y=np_destino, s=np_total/100, c=colors,  alpha=0.4)
plt.show()
