import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline

import numpy as np
import pandas as pd

csvfile = open('psd_oilseeds.csv', 'rb')
csvreader = csv.reader(csvfile, quotechar='"', delimiter = ',')

a=0
z=[]

for row in csvreader:
    if row[1] == "Oilseed, Soybean":
        if row[8] == "Production":
            if row[2] == "US":
                if int(row[4]) >= 2005:
                    print row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]
                    z.append(float(row[11]))
                    a+=1


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Soy")
ax1.set_xlabel('year')
ax1.set_ylabel('Production')
ax1.plot(y, c='r', label='the data')
leg = ax1.legend()
plt.show()