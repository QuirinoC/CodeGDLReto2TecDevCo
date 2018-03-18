# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:59:06 2018

@author: oscar
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

path = 'outputMonth/freq_month.csv'

counter = 0
with open(path, newline = '') as f:
    reader = csv.reader(f)
    row1=next(reader)
    for row in reader:
        #print('estación: ',row[0])
        x=[1,2,3,4,5,6,7,8,9,10,11,12]
        y = []
        for i in range(1,13):
            y.append(row[i])
        y = list(map(int, y))
        p1 = np.polyfit(x,y,1)
        if(p1[0]<0):
            None
        else:
            plt.title('Station %s increased demand' %row[0], fontsize = 20)
            plt.xlabel('Month')
            plt.ylabel('Frequencies')
            plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan.',
                      'Feb.', 'Mar.', 'Apr.','May', 'Jun', 'Jul', 'Aug.',
                      'Sept.', 'Oct.', 'Nov.', 'Dec.'])
            plt.plot(x,y,'o')
            plt.plot(x,np.polyval(p1,x),'r-')
            fig=plt.gcf()
            #print("p1 is: ", p1[0])
            plt.draw()
            fig.savefig('entregables/increasedDemandGraphs/Station_%s_increased_demand.png' %row[0], dpi=100)
            plt.clf()
            #plt.show()
            counter = counter + 1


#print("No. of stations with increased demand: ", counter)
