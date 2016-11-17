import scipy.signal as spysig
import numpy as np
import control  
import matplotlib.pyplot as plt
import seaborn as sns
R1 = 35
R2 = 35
C = 20e-3
R = 0.005
Q = 0.25
num = [1/(R1*C)]
den = [1, ((1/(R1*C)) + (1/(R2*C)))]
A, B, C, D = spysig.tf2ss(num, den)

K, S, E = control.lqr(A[0],B[0],Q,R)

sys = control.ss(A[0] - B[0]*K[0], B[0]*K[0], C, D);
print sys
T, yout = control.step_response(sys)

plt.figure()
plt.plot(T, yout)
plt.show()
