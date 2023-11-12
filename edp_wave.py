import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
programme pour simuler la propagation d'une onde en 1D sur une longueur de 10cm.

pour pouvoir avoir une solution la plus cohérente avec la physique, la condition CFL est utilisé
pour choisir nos paramètres. Cette condition dis que udt/dx = CFL
"""




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
    return np.exp(-(x-x_init)**2/dx)


U = init_cond(x)
Uold = U.copy()
Unew = np.zeros_like(x)



"""
for i in range(0,Nt):
    Unew[1:-1] = (c*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
    Uold = U.copy()
    U = Unew.copy()

"""


fig = plt.figure()
ax = plt.axes(xlim= (0,L) , ylim= (-0.60,1))

line, = ax.plot(x, U)

def update(frame):
    global U, Uold, Unew

    Unew[1:-1] = (c*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
    Uold = U.copy()
    U = Unew.copy()
    
    
    line.set_ydata(U)
    return line,


anim = animation.FuncAnimation(fig,update,frames = Nt, interval = 10,blit = False)
plt.show()