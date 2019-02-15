# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:04:14 2019

@author: bakerb1
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

### create an array of 20 bond lengths spanning 0.5 - 3.5 angstroms
### but store in atomic units of length... note 1 angstrom = 1.88973 a.u. of length
r_array = np.linspace(0.5,3.5,20)*1.88973
print(r_array)

### fill in this array with your actual energy values... there should be 20 values in total!!!
E_array = [-107.142,-110.874,-112.204,-112.622,-112.699,-112.653,-112.570,-112.484,-112.410,-112.361,-112.333,-112.315,-112.303,-112.069,-112.291,-112.287,-112.001,-111.948,-111.927,-112.280 ]


# TO see the plot of the PES, uncomment the following lines
plt.plot(r_array, E_array, 'red')
plt.show()