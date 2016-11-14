import control
import numpy as np
import matplotlib.pyplot as plt

mRod = 1.0
mBall = 1.0
L = 1.0
g = 9.8

I = (1/12.0)*mRod*L**2.0 + (1/4.0)*mBall*L**2.0
print I
tranFun = -1*control.tf([1], [1, 0, -(mBall*g)/I])
print tranFun
T, yout = control.step_response(tranFun)

plt.figure()
plt.plot(T, yout)
plt.show()
