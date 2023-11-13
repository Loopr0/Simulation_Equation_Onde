import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
programme pour simuler la propagation d'une onde en 1D sur une longueur L.

pour pouvoir avoir une solution la plus cohérente avec la physique, la condition CFL est utilisé
pour choisir nos paramètres. Cette condition dis que udt/dx = CFL
"""



##################################


c = 100 # Vitesse de l'onde
L = 5  # Longueur de la corde
T = 0.1  # Temps total
K = 0.4 #coef d'atténuation au bord
dx = 0.01
dt = 0.0001
Nx = int(L/dx) # Nombre de points spatiaux
Nt = int(T/dt)  # Nombre de pas de temps

x = np.linspace(0,L,Nx)
x_init = L/2 #onde placée au centre de la longueur L


####################################


#définition des conditions initial comme une gaussienne
def init_cond(x):
    return np.exp(-(x-x_init)**2/dx)


#condition au bord : 0 = dirichelet, 1 = Neumann, 2 = sans reflexion
Bord_Lx = 2
Bord_0x = 2

U = init_cond(x)
Uold = U.copy()
Unew = np.zeros_like(x)

###################################



fig = plt.figure()
ax = plt.axes(xlim= (0,L) , ylim= (-0.6,1))
ax.grid()
line, = ax.plot(x, U)


##################################

def update(frame):
    global U, Uold, Unew

    Unew[1:-1] = (c*dt/dx)**2*(U[2:] - 2*U[1:-1] + U[:-2]) + 2*U[1:-1] - Uold[1:-1]
    #en prenant cette intervalle ]0,L[ on ne prend pas en compte les limites au bord qui sont pris en compte dans les if


#condition au limite gauche x = 0
    if Bord_0x == 0:
        U[0] = 0

    elif Bord_0x == 1:
        U[0] = U[1] #dans cette condition, l'amplitude en 0 dois valoir l'amplitude qui arrive sur la paroi

    elif Bord_0x == 2:
        Unew[0] = U[1] + K*( Unew[1] - U[0]) #pb après un certain temps gros bordel venant du bord (arrive plus vite quand K augmente)
        #+ pas bonne valeur d'atténuation


#condition au limite droite x = L
    if Bord_Lx == 0:
        U[-1] = 0

    elif Bord_Lx == 1:
        U[-1] = U[-2]

    elif Bord_Lx == 2:
        Unew[-1] = U[-2] + K*( Unew[-1] - U[-2]) #de ce côté aucun pb pas bonne valeur d'atténuation
    
    
    Uold = U.copy()
    U = Unew.copy()
#pb réglé de bordel en mettant Uold et U ici mais mtn satisfait pas les bonne condition limite à droite (quand 2 fait 1 avec 0)
    line.set_ydata(U)

    return line,


anim = animation.FuncAnimation(fig,update,frames = Nt, interval = 10,blit = False)
plt.show()
