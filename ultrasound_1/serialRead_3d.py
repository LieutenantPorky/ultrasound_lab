#!/usr/bin/env python3

import sys
import serial
import io

print("Serial init")
ser = serial.Serial('/dev/ttyACM0', timeout = 1)
ser.baudrate = 9600

theta_array = []
r_array = []
phi_array = []
logging = False

#sensor offset is distance between gyro and ultrasound in cm
sensor_offset = 7.9

while len(r_array) < 150:
    newLine = ser.read_until()
    print(newLine)

    if logging:
        current = [float(i) for i in newLine.decode("utf-8")[:-2].split(',')]
        if(current[2] > 5 and current[2] < 150):
            phi_array.append(current[0])
            theta_array.append(current[1])
            r_array.append(current[2] + sensor_offset)

    if newLine == b'a\r\n':
        print("------------\nstart logging\n------------")
        logging = True


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (16, 12))

ax = fig.add_subplot(111, projection='3d')

R = np.array(r_array)
theta = np.array(theta_array) * np.pi / 180 + np.pi/2
phi = np.array(phi_array) * np.pi / 180

ax.set_xlim(0,100)
ax.set_ylim(-50,50)
ax.set_zlim(-50,50)

ax.scatter(R * np.sin(theta) * np.cos(phi), R * np.sin(theta) * np.sin(phi), R * np.cos(theta))
# plt.rlabel('Distance (m)')
# plt.thetalabel('Angle ')

plt.show()
