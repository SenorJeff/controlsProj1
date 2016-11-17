import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import seaborn as sns

'''
Rd = 30
Ld = 1.95e-6
Rx = 50
Cx = 7.9e-3
'''
'''
R = .5
L = 1e-3
C = 1e-3
Kp = 100
'''
R1 = 5
R2 = 3
C1 = 1

tf = sig.lti( [1/(R1*C1)], [1,(1/(R1*C1) + 1/(R2*C1))] )

print( "A: ", -(1/(C1*R1) + 1/(C1*R2)) )
print( "B: ", (1/R1*C1) )
print( "C: ", [1, 0])
print( "D: ", 0)
print( "LTI: " , tf)

print( sig.tf2ss(tf.num, tf.den) )
print( sig.ss2tf([-(1/(C1*R1) + 1/(C1*R2))],[(1/R1*C1)], [1], [0]) )
#tf = sig.lti([1], [1, R*C])
#kf = sig.lti( [Kp, Kp*R/L, Kp*1/(L*C)], [Kp, Kp*R/L, Kp*1/(L*C)+1])
#transferFunction = sig.lti( [1/(Rd), 1/(Rx*Rd*Cx)], [1, (1/(Rx*Cx)+1/(Rd*Cx)) ] )

#l = 4/tf

t1, steps1 = sig.step(tf, N=10e3)
#t2, steps2 = sig.step(kf, N=10e3)

fig, ax1 = plt.subplots()

ax1.plot(t1, steps1)
#ax2 = ax1.twinx()
#ax2.plot(t2, steps2, 'r')
#plt.show()
