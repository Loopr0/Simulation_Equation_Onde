import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


"""
programme pour simuler la propagation d'une onde en 1D sur une longueur L avec conditions aux limites telles que:
- reflexion totale (Neumann)
- reflexion totale inversée (Dirichlet)
- sans bord

pour pouvoir avoir une solution la plus cohérente avec la physique, la condition CFL est utilisée pour choisir nos paramètres.
Cette condition dit que udt/dx = CFL
"""

#définition des paramètres du problème
c = 10 # Vitesse de l'onde
L = 5  # Longueur de la corde
T = 2  # Temps total

dx = 0.01
dt = 0.001
Nx = int(L/dx) # Nombre de points spatiaux
Nt = int(T/dt)  # Nombre de pas de temps


x = np.linspace(0,L,Nx)
x_init = L/2 #pour x_init 0 ou L il faut vérifier les conditions de Neumann en ce bord





#définition des conditions initiales comme une gaussienne
def init_cond(x):
    return np.exp(-(x-x_init)**2/0.1)


#conditions aux bords : 0 = Dirichlet, 1 = Neumann, 2 = sans bord
Bord_0x = 0
Bord_Lx = 1

#mise en place des matrices utiles, avec U placée à la condition initiale x_init
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
    print(frame)

    Unew[1:-1] = (c*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]

    Uold = U.copy()
    U = Unew.copy()

#condition au limite gauche x = 0
    if Bord_0x == 0:
        U[0] = 0

    elif Bord_0x == 1:
        U[0] = U[1] #dans cette condition, l'amplitude en 0 doit valoir l'amplitude qui arrive sur la paroi

    elif Bord_0x == 2:
        Unew[0] = U[1] #condition de continuité, propagation sans bord


#condition au limite droite x = L
    if Bord_Lx == 0:
        U[-1] = 0

    elif Bord_Lx == 1:
        U[-1] = U[-2]

    elif Bord_Lx == 2:
        Unew[-1] = U[-2]
    

    line.set_ydata(U)

    return line,


anim = animation.FuncAnimation(fig,update,frames = Nt, interval = 10,blit = False)
plt.show()