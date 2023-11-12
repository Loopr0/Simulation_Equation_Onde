import numpy as np
import matplotlib.pyplot as plt


#dérivé premiere méthode élément finie

Nx = 1000
L = 10
dx = L/Nx
x = np.linspace(0,L,Nx)


f1 = np.zeros_like(x)
f1[0] = 1

for i in range(0,Nx-1):
    Fdx = (1 - dx)*f1[i]
    f1[i+1] = Fdx


plt.plot(x,f1)
plt.show()


#dérivée seconde élément finie

f2 = np.zeros_like(x)
f2[0] = 1



for i in range(1,Nx -1): 
    Fdx2 = (-dx**2 +2)*f2[i]- f2[i-1]
    f2[i+1] = Fdx2


plt.plot(x,f2)
plt.plot(x,np.cos(x)-(1/dx)*np.sin(x))
plt.grid()
plt.show()
