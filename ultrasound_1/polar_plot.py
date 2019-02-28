#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:44:17 2019

@author: chirag
"""

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize = (16, 12))

theta_array = np.linspace(0, 2*np.pi, 1000)
r_array = np.sin(theta_array)

ax = plt.subplot(111, projection='polar')
ax.plot(theta_array, r_array, c='k')

plt.rlabel('Distance (m)')
plt.thetalabel('Angle ')

plt.show()

while True:
    
    ax.plot()