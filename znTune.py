import finalComparison as fc
import control
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 

def znTune(plant):
    k = np.linspace(0.1, 0.1, 1)
    t = []
    y = []

    t, y = fc.NoControl(plant)
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
