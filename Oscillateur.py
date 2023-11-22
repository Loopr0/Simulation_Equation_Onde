import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
oscillateur amortie où le but st d'avoir une amplitude variant au cours du temps à une position précise, le temps ici fais office d'évolution temporelle mais on veut simple point
à une position x0 fixe dont sa postion z évolue en fonction de t. Ce programme sera ajouté au prog principale de l'équation d'onde.

"""


w0 = 8
alpha = 0.5
x = np.linspace(0,10,500)
z0 = 1
zpoint0 = 0


A = np.zeros_like(x)




def f(X,t):
    z,zpoint = X
    return zpoint , -alpha*zpoint - w0**2 * z
    


def sol(z0,zpoint0):
    return odeint(f,[z0,zpoint0],x)

def update(frame):
    A[250] = sol(z0,zpoint0)[frame,0]
    line.set_ydata(A)



fig, ax = plt.subplots()
ax.grid()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
line, = ax.plot(x,A)
    

anim = animation.FuncAnimation(fig,update,frames = 500, interval = 10,blit = False)
plt.show()






#fix le bouclage de frame, càd trouver comment faire pour avoir variable variant dans update sans frame et modifiable ou trouver condition



















"""
Test de l'oscillo sur le prog wavevelocity, c'est pas mal mais à amélioré, voir comment au dessus








#définition des paramètres du problème
L = 50  # Longueur de la corde
T = 0.1  # Temps total
dx = 0.01
dt = 0.001
Nx = int(L/dx) # Nombre de points spatiaux
Nt = int(T/dt)  # Nombre de pas de temps

x = np.linspace(0,L,Nx)
x_init = 0 #onde placée au centre de la longueur L

c = np.zeros_like(x)



alpha = 2
w0 = 5
z0 = 0
zpoint0 = 2


def f(X,t):
    z,zpoint = X
    return zpoint , -alpha*zpoint - w0**2 * z
    


def sol(z0,zpoint0):
    return odeint(f,[z0,zpoint0],x)






#changement de vitesse en x = 2.5
def celer(x):
    if x <= 3:
        return 10
    else:
        return 10

for e in range(0,Nx):
    c[e] = celer(x[e])



#mise en place des matrices utiles, avec U placée au condition initiale x_init
U = np.zeros_like(x)
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
    
    U[int(Nx/2)] = sol(z0,zpoint0)[frame,0]

    Unew[1:-1] = (c[1:-1]*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
    Uold = U.copy()
    U = Unew.copy()

    U[0] = U[1]
    U[-1] = U[-2]
    
    line.set_ydata(U)
    return line,


anim = animation.FuncAnimation(fig,update,frames = 500, interval = 10,blit = False)
plt.show()

"""