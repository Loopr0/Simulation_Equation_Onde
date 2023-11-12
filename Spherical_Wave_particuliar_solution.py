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



x, y = np.meshgrid(np.linspace(-1, 1, 1000), np.linspace(-1, 1, 1000))
r = x**2 + y**2



"""
for t in range(0,100,1):
    fig, ax = plt.subplots()
    ax.contourf(x,y,OPP(t*10**-2,r,k,f))
    fig.subplots_adjust(bottom=0.25)
    plt.show()
"""


fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    ax.contourf(x,y,OPP(i*10**-2,r,k,f))
    ax.set_title(i)


ani = animation.FuncAnimation(fig,animate,100,interval = 100,blit=False)



plt.show()



