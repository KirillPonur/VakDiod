

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
import pandas as pd
fig = plt.figure() 

def F(U_a,U_f):
    x = [0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 15, 20, 40]
    y = [0.03, 0.177, 0.414, 1, 2.57, 4.65, 7.13, 9.94, 16.5, 24.1, 32.5, 53,
            77, 138, 211, 622]
    func = np.polyfit(x,y,4)
    func = np.poly1d(func)
    return func(U_a/U_f)

k = 1.88e-5


file = pd.read_excel('../diod.xlsx')


plt.figure(1)
x0 = np.linspace(0,100,1000)
Un = 4.9 
y=file['I_a3']
y=y[~np.isnan(y)]
x=file['U_a3']
x=x[~np.isnan(x)]
Ja = 2/5 * k * Un**(3/2) * F(x0,Un) * 1000
plt.plot(x0,Ja, markersize=4,label="$J_{\\text{н}}^{\\text{т}}=1.42$, А")
plt.plot(x,y,
'o',markersize=4,color='sandybrown',label='$J_{\\text{н}}^{\\text{п}}=1.42$, А')


Un = 5.1 
y=file['I_a4']
y=y[~np.isnan(y)]
x=file['U_a4']
x=x[~np.isnan(x)]
x0 = np.linspace(0,100,1000)
Ja = 2/5 * k * Un**(3/2) * F(x0,Un) * 1000
plt.plot(x0,Ja, markersize=4,label="$J_{\\text{н}}^{\\text{т}}=1.46$, А")
plt.plot(x,y, 'o',markersize=4,label='$J_{\\text{н}}^{\\text{п}}=1.46$, А')

Un = 5.4 
x0 = np.linspace(0,100,1000)
y=file['I_a5']
y=y[~np.isnan(y)]
x=file['U_a5']
x=x[~np.isnan(x)]
Ja = 2/5 * k * Un**(3/2) * F(x0,Un) * 1000
plt.plot(x0,Ja, markersize=4,label="$J_{\\text{н}}^{\\text{т}}=1.50$, А")
plt.plot(x,y, 'o',markersize=4,label='$J_{\\text{н}}^{\\text{п}}=1.50$, А')

plt.xlabel('$U_{\\text{а}}$, В')
plt.ylabel('$I_{\\text{а}}$, мА')
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.minorticks_on()
plt.legend(fontsize=12)
plt.savefig('fig6.pdf',bbox_inches='tight')
plt.show()
