import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
oscillateur amorti où le but est d'avoir une amplitude variant au cours du temps à une position précise, le temps ici fait office d'évolution temporelle mais on veut un simple point à une position x0 fixe dont sa postion z évolue en fonction de t. Ce programme sera ajouté au programme principal de l'onde en 2D. L'oscillateur fonctionne pour un temps T long, si T n'est pas assez long il redémarerra et il y aura 2 propagations dans le milieu.

Choix à faire : simple = oscillateur sans propagation, propagation = oscillateur avec propagation (évolution de simple)

"""

choixosci = "simple"


def f(X,t):
    z,zpoint = X
    return zpoint , -alpha*zpoint - w0**2 * z


def sol(z0,zpoint0):
    return odeint(f,[z0,zpoint0],x) #calcul des solutions

def celer(x):
    if x <= 3:
        return 10
    else:
        return 10

#partie oscillateur simple
if choixosci == "simple":

    w0 = 8
    alpha = 2
    x = np.linspace(0,10,300)
    z0 = 1
    zpoint0 = 0

    A = np.zeros_like(x)

    def update(frame):
        if frame<len(A):
            A[frame] = sol(z0,zpoint0)[frame,0]
            line.set_ydata(A)


    fig, ax = plt.subplots()
    ax.grid()
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    line, = ax.plot(x,A)


    anim = animation.FuncAnimation(fig,update,frames = 500, interval = 10,blit = False)
    plt.show()


#oscillateur avec propagation (changement de vitesse possible)

if choixosci == "propagation":
    L = 10
    T = 2
    dx = 0.01
    dt = 0.001
    Nx = int(L/dx)
    Nt = int(T/dt)

    x = np.linspace(0,L,Nx)
    x_init = int(Nx/2) #onde placée au centre de la longueur L

    c = np.zeros_like(x)


    #parametres oscillateur
    alpha = 2
    w0 = 5
    z0 = 0
    zpoint0 = -2


    for e in range(0,Nx):
        c[e] = celer(x[e])



    U = np.zeros_like(x)
    Uold = U.copy()
    Unew = np.zeros_like(x)



    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    ax.set_ylim(-1, 1)
    ax.grid()
    line, = ax.plot(x, U)



    def update(frame):
        global U, Uold, Unew

        if frame <= 500:     #nombre suffisament grand pour que l'oscillateur tende vers sa position d'équilibre pour éviter un effet de superposition
            U[x_init] = sol(z0,zpoint0)[frame,0]

        Unew[1:-1] = (c[1:-1]*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
        Uold = U.copy()
        U = Unew.copy()

        U[0] = U[1]
        U[-1] = U[-2]

        line.set_ydata(U)
        return line,


    anim = animation.FuncAnimation(fig,update,frames = Nt, interval = 10,blit = False)
    plt.show()