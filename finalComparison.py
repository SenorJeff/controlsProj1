import control
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import seaborn as sns

s = control.tf([1, 0], [1])
R1 = 35
R2 = 35
C = 20e-3


def NoControl(plant):
    return control.step_response(plant)

def PIDControl(plant):
    kP = 1 
    kI = 1
    kD = 1 
    P = kP
    I = kI/s
    D = s*kD

    output = (P+I+D)*plant / (1 + (P+I+D)*plant)

    return control.step_response(output)

def LQRControl(plant):
    R = 0.005
    Q = 0.25

    plantStateSpace = control.tf2ss(plant)
    K, P, E = control.lqr(plantStateSpace,Q,R)
    
    output = control.ss(A[0] - B[0]*K[0], B[0]*K[0], C, D);
    return control.step_response(output)


if __name__ == "__main__":
    plant = (1/(R1*C))/(s + (1/R2*C) + (1/(R1*C))) 

    t1, y1 = NoControl(plant)
    t2, y2 = PIDControl(plant)
    t3, y3 = LQRControl(plant)
