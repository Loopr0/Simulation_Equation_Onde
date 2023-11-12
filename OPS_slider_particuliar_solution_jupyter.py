"""
le code permet de simuler une corde de guitare en vue de coté avec matplotlib.
on peut interagir avec un slider pour modifier le temps t ce qui nous montre
la variation de l'amplitude durant le temps.
"""

import matplotlib.pyplot as plt
from ipywidgets import interact, widgets
import numpy as np


ld = 0.5 #m
L = ld #m/s
x = np.linspace(0,L,1000) #m

def OP(t):
    c = 20 #m/s
    f = c/2*L #s-1
    k = 2*np.pi/ld #m-1
    
    plt.plot(x, 10*np.cos(2*np.pi*f*t)*np.sin(k*x))
    plt.ylim([-11,11])
    plt.show()

# curseur interractif
interact(OP, t=widgets.FloatSlider(min=0, max=10**-1, step=20**-2, value=1.0))