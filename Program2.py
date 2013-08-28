"""
Program to plot the Power Angle Characteristics of a Salient Pole Synchronous Generator
"""

from matplotlib.pyplot import *
from math import sin, cos, atan
from numpy import *

Vt = 1.0		#input('Enter the per phase voltage: ')
Ia = 0.4 - 1j*0.3 	#input('Enter the phase current: ')
Xd = 0.8		#input('Enter the phase d-axis reactance: ')
Xq = 0.3		#input('Enter the phase q-axis reactance: ')

theta = abs(angle(Ia))
delta = ( abs(Ia)*Xq*cos(theta) ) / ( Vt + abs(Ia)*Xq*sin(theta) ) 
delta = atan(delta)
delta = abs(delta)

Iq = Ia*cos(theta+delta)
Id = Ia*sin(theta+delta)
Eg = Vt + 1j*Xd*Id + 1j*Iq*Xq
Egm = abs(Eg)
Eg_check = abs(Vt*cos(delta) + abs(Id)*Xd)

del_vect = arange(0, pi, 0.01)			#similar to 0:0.01:pi in matlab
Psyn_max = abs(Eg*Vt/Xd)
Prel_max = abs(Vt)**2 * (Xd-Xq) / (2*Xd*Xq)

Psyn = Psyn_max * sin(del_vect)
Prel = Prel_max * sin(2*del_vect)
Pl = Psyn+Prel

plot(del_vect, Psyn, 'red', del_vect, Prel, 'blue', del_vect, Pl, 'green')
legend(['Synchronous Power', 'Reluctance Power', 'Load Power'])
xlabel('Power Angle(delta)')
ylabel('Power')
title('Power Angle Characteristics of a Salient Pole Synchronous Generator')
grid()		#similar to 'grid on' in matlab
show()		#you need to use this to show the figure after plotting
