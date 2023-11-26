"""
évolution du slider sans utiliser jupyter
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

def OPS(time,x,k,f):
    return np.cos(2*np.pi*f*time)*np.sin(k*x)


ld = 0.5 #m
L = 2*ld #m/s

init_time = 0
x = np.linspace(0,L,1000) #m

c = 20 #m/s
f = c/2*L #s-1
k = 2*np.pi/ld #m-1


fig, ax = plt.subplots()
line, = ax.plot(x,OPS(init_time,x,k,f))
ax.set_xlabel("position x en m")

#déplace le plot pour laisser de la place au slider
fig.subplots_adjust(bottom=0.25)

#slider pour le temps sur horizontal
axtime = fig.add_axes([0.25, 0.1, 0.65, 0.03])
time_slider = Slider(
    ax=axtime,
    label="temps en s",
    valmin=0,
    valmax=2,
    valinit=init_time
)

#fonction pour update le graphique
def update(val):
    line.set_ydata(OPS(time_slider.val,x,k,f))
    fig.canvas.draw_idle()

#conserve les updates du slider donc on peut le déplacer
time_slider.on_changed(update)


plt.show()
