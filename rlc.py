import control
import numpy as np
import matplotlib.pyplot as plt

R1 = 35
R2 = 35
C = 20e-3
kP = 1 
kI = 1
kD = 1 
s = control.tf([1, 0], [1])

plant = (1/(R1*C))/(s + (1/R2*C) + (1/(R1*C))) 

P = kP
I = kI/s
D = s*kD

PID = P + I + D

#system = PID*plant/(1+PID*plant)
system = plant
print system
T1, yout1 = control.step_response(system)

plt.plot(T1, yout1)
plt.show()
