import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import scipy as sp
fig = plt.figure() 
ax = fig.add_subplot(111) 

file = pd.read_excel('../diod.xlsx')

y = file['T']
x = file['I_накала']

x = x[~np.isnan(x)]
y = y[~np.isnan(y)]


func = np.polyfit(x,y,1)
print(func)
ax.plot(x,y,'ko-', color = "darkslateblue", markersize=4) 
plt.xlabel('$J_{\\text{н}}$, мА')
plt.ylabel('$T$, К ')
plt.savefig('lengmur.pdf',bbox_inches='tight')
plt.show()
