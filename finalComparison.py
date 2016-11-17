import control
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import seaborn as sns

s = control.tf([1, 0], [1])
R1 = 35
R2 = 35
C = 20e-3
T = np.linspace(0, 10, 10000)

def NoControl(plant):
    return control.step_response(plant, T)

def PIDControl(plant):
    kP = 1
    kI = 1
    kD = 0 
    P = kP
    I = kI/s
    D = s*kD
    PID = P + I + D

    output = (PID*plant) / (1 + PID*plant)

    return control.step_response(output, T)

def LQRControl(plant):
    R = 0.005
    Q = 0.25

    plantStateSpace = control.tf2ss(plant)
    A, B, C, D =  control.ssdata(plantStateSpace)
    K, P, E = control.lqr(plantStateSpace,Q,R)
    output = control.ss(A[0] - B[0]*K[0], B[0]*K[0], C, D);
    return control.step_response(output, T)


if __name__ == "__main__":
    plant = (1/(R1*C))/(s + (1/R2*C) + (1/(R1*C))) 

    t1, y1 = NoControl(plant)
    t2, y2 = PIDControl(plant)
    t3, y3 = LQRControl(plant)

    plt.figure()
    l1, = plt.plot(t1, y1, label="No Control")
    l2, = plt.plot(t2, y2, label="PID Control")
    l3, = plt.plot(t3, y3, label="LQR Control")
    plt.legend(handles=[l1,l2,l3])
    plt.show()
