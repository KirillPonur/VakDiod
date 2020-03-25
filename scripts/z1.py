import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
import pandas as pd
fig = plt.figure() 

file = pd.read_excel('../diod.xlsx')

plt.figure(1)
y=file['I_a1']
x=file['U_a1'] 
plt.plot(x,y,'ko', color = "sandybrown", markersize=4,
        label='$I_{\\text{н}} = 1.48$ А') 
plt.xlabel('$U_a$, В') 
plt.ylabel('$J_a$, мА') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig1.pdf',bbox_inches="tight")

plt.figure(2)
y=file['I_a2']
x=file['U_a2'] 
plt.plot(x,y,'ko', color = "teal", markersize=4,
        label='$I_{\\text{н}} = 1.498$ А') 
# plt.title('ВАХ диода при токе накала 1.48 А')
plt.xlabel('$U_{\\text{а}}$, В') 
plt.ylabel('$J_{\\text{а}}$, мА') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig2.pdf',bbox_inches="tight")


plt.figure(3)
y=file['I_a3']
x=file['U_a3'] 
plt.plot(x,y,'ko', color = "darkslateblue", markersize=4,
        label='$I_{\\text{н}} = 1.421$ А') 

y=file['I_a4']
x=file['U_a4'] 
plt.plot(x,y,'ko', color = "teal", markersize=4,
        label='$I_{\\text{н}} = 1.46$ А') 

y=file['I_a5']
x=file['U_a5'] 
plt.plot(x,y,'ko', color = "sandybrown", markersize=4,
        label='$I_{\\text{н}} = 1.498$ А') 

plt.xlabel('$U_{\\text{а}}$, В') 
plt.ylabel('$J_{\\text{а}}$, мА') 
plt.legend()
plt.grid(which='major',linestyle='-') 
plt.grid(which='minor',linestyle=':') 
plt.minorticks_on()
plt.savefig('fig3.pdf',bbox_inches="tight")
plt.show()
