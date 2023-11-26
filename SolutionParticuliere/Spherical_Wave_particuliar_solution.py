import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



ld = 0.5
L = ld
k = 2*np.pi/ld
c = 20 #m/s
f = c/2*L #s-1
init_time = 0

def OPP(time,r,k,f):
    return np.cos(2*np.pi*f*time-k*r)



x, y = np.meshgrid(np.linspace(-1, 1, 500), np.linspace(-1, 1, 500))
r = x**2 + y**2



"""
for t in range(0,100,1):
    fig, ax = plt.subplots()
    ax.contourf(x,y,OPP(t*10**-2,r,k,f))
    fig.subplots_adjust(bottom=0.25)
    plt.show()
"""


fig = plt.figure()
ax = plt.axes(projection='3d')


def animate(i):
    ax.clear()
    #ax.contourf(x,y,OPP(i*10**-2,r,k,f))
    ax.plot_surface(x, y, OPP(i*10**-2,r,k,f), cmap='viridis')
    ax.set_title(i)


ani = animation.FuncAnimation(fig,animate,100,interval = 10,blit=False)




#solution temps calcul framerate bien
Writer = animation.writers['ffmpeg']
writer = Writer(fps=25, bitrate=1800)
ani.save('test3D.mp4', writer=writer)


#ani.save('myani.mp4',writer='ffmpeg',fps=10) #solution simple pas opti
