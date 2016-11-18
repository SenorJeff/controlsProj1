import control
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import seaborn as sns

s = control.tf([1, 0], [1])
T = np.linspace(0, 10, 10000)

def NoControl(plant):
    return control.step_response(plant, T)

def PIDControl(plant, Kp, Ki, Kd):
    P = Kp
    I = Ki/s
    D = s*Kd
    PID = P + I + D

    output = (PID*plant) / (1 + PID*plant)

    return control.step_response(output, T)

def LQRControl(plant, Q, R):

    plantStateSpace = control.tf2ss(plant)
    A, B, C, D =  control.ssdata(plantStateSpace)
    print(A, B, C, D)
    K, P, E = control.lqr(plantStateSpace,Q,R)
    output = control.ss(A - B*K, B*K, C, D);
    return control.step_response(output, T)


def firstOrderSystem():
    R1 = 35
    R2 = 35
    C = 20e-3
    plant = (1/(R1*C))/(s + (1/R2*C) + (1/(R1*C))) 

    Kp = 1
    Ki = 1
    Kd = 0 
    R = 0.05 
    Q = 10
    PIDTuning = [ Kp, Ki, Kd ]
    LQRTuning = [ Q, R ]
    return plant, PIDTuning, LQRTuning

def secondOrderSystem():
    R = 35
    C = 20e-3
    L = 4e-3
    plant = (s/C) / (s**2 + s/(R*C) + 1/(L*C))

    Kp = 1
    Ki = 1
    Kd = 0
    R = 0.05
    Q = 10 

    PIDTuning = [ Kp, Ki, Kd ]
    LQRTuning = [ Q, R ]
    return plant, PIDTuning, LQRTuning


def znTune(plant):
    k = np.linspace(0.1, 0.1, 1)
    t = []
    y = []

    t, y = NoControl(plant)
    tConst = 0.0
    for i in range(0, len(y) - 1):
        if y[i] > 0.63:
            tConst = t[i]
	    kU = y[i]
            break 
        

    Kc = 0.6*tConst/kU
    Tu = tConst

    kP = 0.6*Kc
    kI = 2*kP/Tu
    kD = .125*Tu*kP

    return kP, kI, kD

if __name__ == "__main__":
    plant, PIDTuning, LQRTuning = firstOrderSystem()
    # plant, PIDTuning, LQRTuning = secondOrderSystem()
    kP, kI, kD = znTune(plant)
    t1, y1 = NoControl(plant)
    t2, y2 = PIDControl(plant, kP, kI, kD)
    t3, y3 = LQRControl(plant, LQRTuning[0], LQRTuning[1])

    plt.figure()
    l1, = plt.plot(t1, y1, label="No Control")
    l2, = plt.plot(t2, y2, label="PID Control")
    l3, = plt.plot(t3, y3, label="LQR Control")
    plt.legend([l1,l2,l3])
    plt.show()
