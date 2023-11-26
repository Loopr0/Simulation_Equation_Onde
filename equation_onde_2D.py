
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

typeplot = "3D"
save = True


c = 5 # Vitesse de l'onde
a = 1  # longueur de l'espace
b = a #largeur de l'espace
T = 1  # Temps total (utile quand save animation)

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

x_init = 0.5
y_init = 0.5


def init_cond(x,y):
    return np.exp(-((x-x_init)**2+(y-y_init)**2)/0.01)



U = init_cond(X,Y)
Uold = U.copy()
Unew = np.zeros((Nx,Ny))




#pour 3D
if typeplot == "3D":
    fig = plt.figure()
    ax = plt.axes(projection='3d')



#pour 2D
elif typeplot == "2D":
    fig, ax = plt.subplots()
    fig.tight_layout()
    surface = plt.pcolormesh(X, Y, U, cmap = plt.cm.viridis)
    fig.colorbar(surface)







#fonction pour l'animation en 3D, différent des autres cas, mets à jour le plot (x,y, amplitude) à chaque frame
def update_3D(frame):
    global U, Uold, Unew

    Unew[1:-1,1:-1] = (c*dt)**2 * ((U[2:,1:-1] + U[:-2,1:-1]) / dx**2 + (U[1:-1,2:] + U[1:-1,:-2]) / dy**2 - 2*U[1:-1,1:-1] * (1 / dx**2 + 1 / dy**2)) + 2*U[1:-1,1:-1] - Uold[1:-1,1:-1]

    
    Uold = U.copy()
    U = Unew.copy()


    #condition au bord (à revoir)
    Unew[-1,:] = U[-1,:]
    Unew[:,-1] = U[:,-1]

    Unew[0,:] = U[0,:]
    Unew[:,0] = U[:,0]

    
    ax.clear()
    ax.set_zlim((-0.5,0.5))
    ax.plot_surface(X,Y,U,cmap='viridis')



#fonction pour l'animation en 2D utilise le même principe que dans le prog en 1D (mets à jour les données d'amplitude à chaque frame)
def update_2D(frame):
    global U, Uold, Unew

    Unew[1:-1,1:-1] = (c*dt)**2 * ((U[2:,1:-1] + U[:-2,1:-1]) / dx**2 + (U[1:-1,2:] + U[1:-1,:-2]) / dy**2 - 2*U[1:-1,1:-1] * (1 / dx**2 + 1 / dy**2)) + 2*U[1:-1,1:-1] - Uold[1:-1,1:-1]

    
    Uold = U.copy()
    U = Unew.copy()


    surface.set_array(U)

    
    #condition au bord (à revoir)
    Unew[-1,:] = U[-1,:]
    Unew[:,-1] = U[:,-1]

    Unew[0,:] = U[0,:]
    Unew[:,0] = U[:,0]


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
    anim.save('onde2D.mp4', writer=writer)
