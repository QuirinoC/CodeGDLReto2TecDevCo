import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import operator
import csv
import time
import datetime

hours = pd.read_csv('output/horas.csv')

plt.bar(hours['Horas'], hours['Frecuencia'], color ='cyan', alpha = 0.5)
plt.title('Frecuencia en las horas de uso')
plt.ylabel('Frecuencia')
plt.xlabel('Horas')
plt.title('Frecuencia de uso por hora')

plt.show()
