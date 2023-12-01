
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint


"""
Prog pour simuler propagation d'une onde sphérique (cond init en x^2 + y^2) dans espace 2D. Condition au bord, Neumann pour avoir réflexion
sans inverser l'amplitude de l'onde (ou condition sans bord ?? plus juste car pas dans milieu dispersif)

Choix à faire, soit typeplot = 2D ou 3D pour savoir comment plot l'onde 2D. Si save = True faire attention à T car cela peut durée longtemps dans le cas
de 3D plot
pour 2D plot taile espace plus grand possible
"""
typeplot = "2D"
save = False
oscillo = False


zut = 100

c = 5 # Vitesse de l'onde
a = 1  # longueur de l'espace
b = a #largeur de l'espace
T = 1  # Temps total (utile quand save animation et modif quand oscillo)


dx = 0.01
dy = 0.01
dt = 0.001

Nx = int(a/dx) # Nombre de points spatiaux x
Ny = int(a/dy) # Nombre de points spatiaux y
Nt = int(T/dt)  # Nombre de pas de temps


x = np.linspace(0,a,Nx)
y = np.linspace(0,b,Ny)

#création de du plan d'espace
X, Y = np.meshgrid(x,y)

if oscillo:
    x_init = int(Nx/2)
    y_init = int(Ny/2)
    #centre de l'espace

else:
    x_init = 0.5
    y_init = 0.5


#parametres oscillo
alpha = 5
w0 = 10
z0 = 0
zpoint0 = -5
t = np.linspace(0,1,zut) #durée d'intégration oscillo, variable 3 modifie la vitesse de l'oscillation dans la période temporelle (variable 1 et 2)


#####fonction pour oscillateur#####

def f(X,t):
    z,zpoint = X
    return zpoint , -alpha*zpoint - w0**2 * z        


def sol(z0,zpoint0):
    return odeint(f,[z0,zpoint0],t)

###########################

def init_cond(x,y):
    return np.exp(-((x-x_init)**2+(y-y_init)**2)/0.01)


if oscillo:
    U = np.zeros((Nx,Ny))
else:
    U = init_cond(X,Y)
    

Uold = U.copy()
Unew = np.zeros((Nx,Ny))




#pour 3D
if typeplot == "3D": #3D utile quand grande différence d'amplitude
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    fig.tight_layout



#pour 2D
elif typeplot == "2D":
    fig, ax = plt.subplots()
    fig.tight_layout()
    surface = plt.pcolormesh(X, Y, U, cmap = plt.cm.viridis)
    fig.colorbar(surface)



#fonction pour l'animation en 3D, différent des autres cas, mets à jour le plot (x,y, amplitude) à chaque frame
def update_3D(frame):
    global U, Uold, Unew

    if oscillo and frame<zut:
        U[x_init,y_init] = sol(z0,zpoint0)[frame,0] #pb frame et integrale sur t, t trop long donc prend du temps, si t moins de point marche mieux mais sur intervalle de temps court
        #en gros va prendre tout les point de temps Nt pour faire l'osci
        #donne résultat interressant pour zut = 0.01 amplitude petite mais oscilo boucle donc pas ouf

    Unew[1:-1,1:-1] = (c*dt)**2 * ((U[2:,1:-1] + U[:-2,1:-1]) / dx**2 + (U[1:-1,2:] + U[1:-1,:-2]) / dy**2 - 2*U[1:-1,1:-1] * (1 / dx**2 + 1 / dy**2)) + 2*U[1:-1,1:-1] - Uold[1:-1,1:-1]

    
    Uold = U.copy()
    U = Unew.copy()


    #condition au bord de dirichelet car onde à la surface de l'eau n'a pas de vitesse sur la paroi
    

    
    ax.clear()
    ax.set_zlim((-0.5,0.5))
    ax.plot_surface(X,Y,U,cmap='viridis')



#fonction pour l'animation en 2D utilise le même principe que dans le prog en 1D (mets à jour les données d'amplitude à chaque frame)
def update_2D(frame):
    global U, Uold, Unew
    print(frame)

    if oscillo and frame<zut:
        U[x_init,y_init] = sol(z0,zpoint0)[frame,0]

    Unew[1:-1,1:-1] = (c*dt)**2 * ((U[2:,1:-1] + U[:-2,1:-1]) / dx**2 + (U[1:-1,2:] + U[1:-1,:-2]) / dy**2 - 2*U[1:-1,1:-1] * (1 / dx**2 + 1 / dy**2)) + 2*U[1:-1,1:-1] - Uold[1:-1,1:-1]

    
    Uold = U.copy()
    U = Unew.copy()


    surface.set_array(U)

    
    #condition au bord de dirichelet car onde à la surface de l'eau n'a pas de vitesse sur la paroi



    return surface,



if typeplot == "2D":
    anim = animation.FuncAnimation(fig,update_2D,frames = Nt, interval = 50,blit = False)
    plt.show()



if typeplot == "3D":
    anim = animation.FuncAnimation(fig,update_3D,frames = Nt, interval = 50,blit = False)
    plt.show()


if save:
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=24, bitrate=1800)
    anim.save('onde2DJSP.mp4', writer=writer)
