import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

# x=np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44]) 
# y=np.array([0,1,8,14,28,38,54,74,100]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 


x=np.array([0,1.3,2.2,2.9,4.2,5.4,6.7,7.8,8.9,9.9,10.8,11.8,12.8,13.7,14.6,15.4,16.3,17.1,18.1,19.1,20.3,21.5,23.4,37.7,39.7,47.3,59.7,75.3,79.8,106.4,115.7,119,120]) 
y=np.array([0.13,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.21,1.31,1.41,1.51,1.61,1.71,1.83,1.94,2.06,2.14,2.2,2.25,2.26,2.27,2.3,2.31,2.32,2.35,2.36,2.36,2.36]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 


# x=np.array([0,19.8,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]) 
# y=np.array([0,0.008,0.015,0.022,0.033,0.059,0.071,0.092,0.13,0.17,0.227,0.301,0.375,0.455,0.62,0.74,0.985]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

# plt.legend(('$\phi_з=40В$','$\phi_з=45В$','$\phi_з=50В$'),loc=(0.1,0.4))

ax.plot(x,y,'ko', color = "darkslateblue", markersize=4) 
plt.title('ВАХ диода при токе накала 1.48 А')
plt.xlabel('$U_a$,В') 
plt.ylabel('$J_a$,мА') 
plt.grid () 
plt.xlim([-1,130]) 
plt.ylim([0,2.5]) 
plt.savefig('z1.png',dpi=300)
plt.show()