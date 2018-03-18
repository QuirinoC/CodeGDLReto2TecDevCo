# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:59:06 2018

@author: oscar
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from heapq import nlargest
path = 'outputMonth/freq_month.csv'
allStations = {}
ten_largest = {}
counter = 0

plt.title('Stations increased demand')
plt.xlabel('Month')
plt.ylabel('Frequencies')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan.',
           'Feb.', 'Mar.', 'Apr.','May', 'Jun', 'Jul', 'Aug.',
           'Sept.', 'Oct.', 'Nov.', 'Dec.'])


with open(path, newline = '') as f:
    reader = csv.reader(f)
    row1=next(reader)
    for row in reader:
        print('estación: ',row[0])
        x=[1,2,3,4,5,6,7,8,9,10,11,12]
        y = []
        for i in range(1,13):
            y.append(row[i])

        y = [int(i) for i in y]
        p1 = np.polyfit(x,y,1)
        #fig=plt.gcf()
        allStations[row[0]] = p1[0]
        #fig.savefig('C:\\Users\\oscar\\Desktop\\CodeGDL\\CodeGDLReto2TecDevCo\\outputMonth\\increasedDemandGraphs\\Station_%s_increased_demand.png' %row[0], dpi=100)
        counter = counter + 1

ten_largest = nlargest(10, allStations, key=allStations.get)

with open(path, newline = '') as f:
    reader = csv.reader(f)
    row1=next(reader)
    for row in reader:
        x=[1,2,3,4,5,6,7,8,9,10,11,12]
        y = []
        for i in range(1,13):
            y.append(row[i])
        y = [int(i) for i in y]
        str_row = row[0] + ""
        print("row[0] is:", row[0])
        print("ten_largest is:", ten_largest)
        for i in ten_largest:
            if(str_row == i):
                p1 = np.polyfit(x,y,1)
                plt.plot(x,y,'o')
                plt.plot(x,np.polyval(p1,x),'r-')

plt.show()
print("No. of stations with increased demand: ", counter)
