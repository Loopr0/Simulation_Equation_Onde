import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
programme pour simuler la propagation d'une onde en 1D avec changement de vitesse en x = 3 les conditions
au bord son ce de Neumann et la vitesse est divisé par 2. Attention lors d'un changement de vitesse
rester en condition CFL
"""

#définition des paramètres du problème
L = 5  # Longueur de la corde
T = 0.1  # Temps total
dx = 0.01
dt = 0.0001
Nx = int(L/dx) # Nombre de points spatiaux
Nt = int(T/dt)  # Nombre de pas de temps

x = np.linspace(0,L,Nx)
x_init = 0 #onde placée au centre de la longueur L

c = np.zeros_like(x)



#définition des conditions initial comme une gaussienne
def init_cond(x):
    return np.exp(-(x-x_init)**2/0.1)

#changement de vitesse en x = 2.5
def celer(x):
    if x <= 3:
        return 50
    else:
        return 100

for e in range(0,Nx):
    c[e] = celer(x[e])




#mise en place des matrices utiles, avec U placée au condition initiale x_init
U = init_cond(x)
Uold = U.copy()
Unew = np.zeros_like(x)



#initialisation de la figure et de la courbe du plot
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)
ax.grid()
line, = ax.plot(x, U)


def update(frame):
    global U, Uold, Unew

    Unew[1:-1] = (c[1:-1]*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
    Uold = U.copy()
    U = Unew.copy()

    U[0] = U[1]
    
    line.set_ydata(U)
    return line,


anim = animation.FuncAnimation(fig,update,frames = Nt, interval = 10,blit = False)
plt.show()
