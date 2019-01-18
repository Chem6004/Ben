# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#print("Hello World!")
import numpy as np
#m = 1.0
#v = 5.0
#T = 0.5*m*v*2
#T2 = 1/2*m*v*v
#T3 = 0.5*m*v*v
#T4 = m*v*

m1 = 1.0
v1 = 5.0
q1 = 1.0
x1 = 0.0

m2 = 1.0
v2 = 2.5
q2 = 1.0
x2 = 0.5

r12 = np.sqrt((x1-x2)**2)
v12 = q1*q2/r12
print("separation is", r12)
print("potential energy is ", v12)

import numpy as np
Npart = 10
m = np.zeros (Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros (Npart)

print (m)

for i in range (0,Npart):
    m(i)= 1.0
    q(i)= 1.0
    x(i)= 0.5*1
    v= 0.2*1
    
    


