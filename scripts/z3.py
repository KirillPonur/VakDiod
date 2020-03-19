import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

x=np.array([0,5,10.1,15,18.7,20.6,26.4,31.2,35.5,41.1,46,48.1,54,60,64.6,70.8,75.8,80.6,85.6,90.7,96,100,106,109.6,114.8,120]) 
y=np.array([0,0.63,2.43,4.72,6.33,6.83,7.12,7.2,7.26,7.32,7.36,7.38,7.43,7.47,7.5,7.55,7.58,7.61,7.64,7.67,7.69,7.71,7.75,7.76,7.79,7.82]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 
ax.plot(x,y,'ko', color = "rebeccapurple", markersize=4) 

x=np.array([0,2.4,5.6,10.1,15,20.5,25.1,30.3,36,41.1,45.7,51,55.5,60,66,70.2,75.4,81,86.6,91,95.5,100,105.2,110.3,115.3,120]) 
y=np.array([0,0.14,0.82,2.5,4.97,8.03,10.2,10.8,10.96,11.05,11.13,11.2,11.26,11.31,11.38,11.42,11.47,11.52,11.57,11.6,11.64,11.68,11.72,11.76,11.8,11.83]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 
ax.plot(x,y,'ko', color = "cadetblue", markersize=4)  

x=np.array([0,5.6,11.1,15,19.5,24.3,30.1,35.6,41.3,45,53,60,65.4,70.9,76.9,81.6,89.8,94.6,100,105.7,109.7,115.3,120]) 
y=np.array([0,0.83,3,5.11,7.89,11.03,14.59,16.02,16.27,16.33,16.58,16.72,16.82,16.9,17,17.06,17.17,17.23,17.3,17.36,17.41,17.48,17.53]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

ax.plot(x,y,'ko', color = "sandybrown", markersize=4) 
ax.legend(('$I_a=1.42 A$','$I_a=1.46 A$','$I_a=1.5 A$'))
plt.title('ВАХ диода при различных токах накала')
plt.xlabel('$U_a$,В') 
plt.ylabel('$J_a$,мА') 
plt.grid () 
plt.xlim([-2,130]) 
plt.ylim([-1,20]) 
plt.savefig('z3.png',dpi=300)
plt.show()
