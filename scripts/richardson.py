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

T = lambda J: func[0]*J + func[1]
J = file['I_анода100'][0:6] # мА
J = J[~np.isnan(J)]
x = 1/T(J)
y = np.log(J) - 2*np.log(T(J))
func = np.polyfit(x,y,1)
phi = func[0]
print(phi,func[1])
approx =  np.poly1d(func)
e = -1.69e-19 # Кл
k = +1.38e-23 # Дж*К
print(phi*k/e)

plt.plot(x,y,'ko',label='эксперимент')
plt.plot(x,approx(x),'-',color="darkblue",label='аппроксимация')
plt.xlabel('$\\frac{1}{T},\\text{ К}^{-1}$')
plt.ylabel('$\\textrm{ln} J_s -  2 \\textrm{ln} T$')
plt.legend()
plt.savefig('richardson.pdf',bbox_inches='tight')
plt.show()
