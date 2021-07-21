import matplotlib.pyplot as plt
import numpy as np
 
  
m = np.arange(1.0,11.0,1)           #m modes
R = np.arange(30.0,35.0,0.01)       #RoC mirror
  
# Creating 2-D grid of features

r1 = 0.998                          #R of mirror
r2 = 0.990
L = 9.1                             #length of cav                                                 
g = 1-(L/R)                         #g
F = (np.pi*((r1*r2)**0.25))/(1-(r1*r2)**0.5)    #Finesse

print("F",F)
#print("G",g)
[X, Y] = np.meshgrid(m, R)
  
fig, ax = plt.subplots(1,1)
  
#Z = 1/(1+((2*F/np.pi)**2)*np.sin(X*np.arccos((1-L/Y)**0.5))**2)**0.5
#Z=  1/(1+((2*F/np.pi)**2)*np.sin(X*np.arccos((1-L/Y)**0.5))**2)**0.5


#relative to fun HOM

Z= 1/((1+((2*F/np.pi)**2)*(np.sin(X*np.arccos((1-L/Y)**0.5)))**2)**0.5)  

# plots filled contour plot
cf = ax.contourf(X, Y, Z)
  
ax.set_title('RoC vs TEM')
ax.set_xlabel('TEM (m)')
ax.set_ylabel('RoC ')
fig.colorbar(cf, ax=ax)  
plt.figure(figsize=(8,8))
plt.show()