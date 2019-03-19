### Import statements
### import time library
import time
### import pyplot as library
from matplotlib import pyplot as plt
### import numpy library
import numpy as np


### Function to compute total kinetic energy given an array of masses and velocities
def Kinetic(mass_array, velocity_array):
    N = len(mass_array)
    Kin = 0.
    for i in range(0,N):
        Kin = Kin + 0.5*mass_array[i]*velocity_array[i]**2
    return Kin

### function to compute potential energy given an array of separations and an array of charges
def Potential(sep_array, charge_array):
    ### presumably the number of particles i the length
    ### of the array of charges
    N = len(charge_array)s equal to
    
    ### initialize the potential energy to zer
    Pot = 0.
    ### nested loop
    for i in range(0,N):
        for j in range(0,N):
            ### do not calculate potential of particle with itself!
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j]
    return Pot


import time
### Number of particles will be 10
Npart_array = [5, 10, 15, 20, 25]
for i in range(0,len(Npart_array)):
        m = np.zeros()
### create an array 'm' and 'v' to store the masses and velocities of the 10 particles... 
### initially, each entry in 'm' and 'v' will be zero, and we will have to assign values later
m = np.zeros(Npart)
v = np.zeros(Npart)

for i in range(0,Npart):
    m[i] = 1.0
    v[i] = 2.5


### Now that values have been assigned, print to confirm they are what you expect
print("Printing array of masses: ",m)
print("Printing array of velocities: ",v)

start = time.time()
T = 1/2 * m * v**2
T_tot = np.sum(T)
end = time.time()
print(end-start)
### confirm that T is indeed an array with an entry for the kinetic energy of each particle
print(T)

### initialize a sum variable to zero
T_tot_loop = 0.

### loop over elements of the T array and 
### compute the sum 
for i in range(0,Npart):
    ### add elements to the sum variable
    T_tot_loop = T_tot_loop + T[i]
    
### compute the sum using np.sum instead
T_tot_sum = np.sum(T)

### print both sums to confirm both methods give the same answer
print("Result from loop is ",T_tot_loop)
print("Result from numpy sum is ",T_tot_sum)

### create 1-D arrays of length Npart for q... assign each particle charge of 1 natural unit
q = np.ones(Npart)

### create a 1-D array of length Npart for x... use np.linspace to automatically
### assign values since we want the particles evenly spaced.
x = np.linspace(0,(Npart-1)*0.2,Npart)

### create a 2-D array that is Npart x Npart for the separations between particle pairs
r = np.zeros((Npart,Npart))

### compute all separations using two nested for-loops to access the positions of each particle
for i in range(0,Npart):
    for j in range(0,Npart):
        r[i][j] = np.sqrt( (x[i]-x[j])**2 )

### now print all arrays 
print("Printing array of charges ",q)
print("Printing array of charges ",x)
print("Printing array of charges \n",r)

### function to compute potential energy given an array of separations and an array of charges
def Potential(sep_array, charge_array):
    ### presumably the number of particles is equal to the length
    ### of the array of charges
    N = len(charge_array)
    
    ### initialize the potential energy to zer
    Pot = 0.
    ### nested loop
    for i in range(0,N):
        for j in range(0,N):
            ### do not calculate potential of particle with itself!
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j]
    return Pot


### Compute total potential energy and store it as the variable V_tot
V_tot = Potential(r, q)

### print it to see what it is!
print(V_tot)

'''
Example of the use of the time and pyplot libraries in python... we will do things:
(1) Create an array of x values and an array of y values and use pyplot to plot them
(2) Measure the time taken to run the entire program
'''
### import time library
import time
### import pyplot as library
from matplotlib import pyplot as plt

### get the time at the beginning of the program
start = time.time()
### create an array of 100 x-values between -5 and 5
x = np.linspace(-5,6,100)
### create an array of y-values defined as y = x^2
y = x**2


### plot y = x^2 with a red line!
plt.plot(x, y, 'red')
plt.xlim(0,6)
plt.ylim(0,36)
plt.show()

### figure out how much time this whole program took to run!
end = time.time()
how_long = end - start
### print the total time taken in seconds
print(" Total time to run in seconds is: ",how_long)

