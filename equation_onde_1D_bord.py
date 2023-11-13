import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
programme pour simuler la propagation d'une onde en 1D sur une longueur L avec condition au limite tels que soit :
- reflexion totale
- reflexion totale inversé
- sans bord

le cas d'une atténuation au bord sera traité dans un autre programme car pas la même équation d'onde.

pour pouvoir avoir une solution la plus cohérente avec la physique, la condition CFL est utilisé pour choisir nos paramètres.
Cette condition dis que udt/dx = CFL
"""

#définition des paramètres du problème
c = 100 # Vitesse de l'onde
L = 5  # Longueur de la corde
T = 0.1  # Temps total

dx = 0.01
dt = 0.0001
Nx = int(L/dx) # Nombre de points spatiaux
Nt = int(T/dt)  # Nombre de pas de temps

x = np.linspace(0,L,Nx)
x_init = L/2 #onde placée au centre de la longueur L





#définition des conditions initial comme une gaussienne
def init_cond(x):
    return np.exp(-(x-x_init)**2/0.1)


#condition au bord : 0 = dirichelet, 1 = Neumann, 2 = sans bord
Bord_Lx = 1
Bord_0x = 1

#mise en place des matrices utiles, avec U placée au condition initiale x_init
U = init_cond(x)
Uold = U.copy()
Unew = np.zeros_like(x)



#initialisation de la figure et de la courbe du plot
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-0.6, 1)
ax.grid()
line, = ax.plot(x, U)


def update(frame):
    global U, Uold, Unew

    Unew[1:-1] = (c*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
    #en prenant cette intervalle ]0,L[ on ne prend pas en compte les limites au bord qui sont pris en compte dans les if

    Uold = U.copy()
    U = Unew.copy()


#condition au limite gauche x = 0
    if Bord_0x == 0:
        U[0] = 0

    elif Bord_0x == 1:
        U[0] = U[1] #dans cette condition, l'amplitude en 0 dois valoir l'amplitude qui arrive sur la paroi

    elif Bord_0x == 2:
        Unew[0] = U[1] + ( Unew[0] - U[1]) #condition de continuité, propagation sans bord


#condition au limite droite x = L
    if Bord_Lx == 0:
        U[-1] = 0

    elif Bord_Lx == 1:
        U[-1] = U[-2]

    elif Bord_Lx == 2:
        Unew[-1] = U[-2] + ( Unew[-1] - U[-2]) 
    

    line.set_ydata(U)

    return line,


anim = animation.FuncAnimation(fig,update,frames = Nt, interval = 10,blit = False)
plt.show()
