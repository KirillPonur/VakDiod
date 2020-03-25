import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
fig = plt.figure() 
ax = fig.add_subplot(111) 

file = pd.read_excel('../diod.xlsx')

plt.figure(1)
y=file['I_анода15']
x=file['I_накала15'] 
ax.plot(x,y,'ko', color = "darkslateblue", markersize=4, 
        label='$U_{\\text{а}} = 15$ В') 

y=file['I_анода60']
x=file['I_накала60'] 
ax.plot(x,y,'ko', color = "sandybrown", markersize=4, 
        label='$U_{\\text{а}} = 60$ В') 

y=file['I_анода100']
x=file['I_накала100'] 
ax.plot(x,y,'ko', color = "teal", markersize=4, 
        label='$U_{\\text{а}} = 100$ В') 

plt.xlabel('$J_{\\text{н}}$, В') 
plt.ylabel('$J_{\\text{а}}$, мА') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig4.pdf',bbox_inches="tight")

plt.show()



