#!/usr/bin/env python3

import sys
import serial
import io
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Setup serial connection and debug

print("Serial init")
ser = serial.Serial('/dev/ttyACM0', timeout = 1)
ser.baudrate = 9600

#arrays to hold incoming serial data

theta_array = []
r_array = []
phi_array = []
logging = False

#sensor offset is frontal distance between gyro and ultrasound in cm
sensor_offset = 0.0

#lateral sensor offset is distance to gyro on y axis (eg when mounting on holder)
lateral_offset = 8.5

while len(r_array) < 150:
    #read serial buffer up to newline character (indicates one package)
    newLine = ser.read_until()
    print(newLine)

    if len(newLine) > 2:

        if logging:
            #if logging flag has been read, save data to buffers
            current = [float(i) for i in newLine.decode("utf-8")[:-2].split(',')]
            if(current[2] > 5 and current[2] < 150):
                phi_array.append(current[0])
                theta_array.append(current[1])
                r_array.append(current[2] + sensor_offset)
    elif logging:
        break

    if newLine == b'a\r\n':
        #look for logging flag
        print("------------\nstart logging\n------------")
        logging = True


#Plot the data

plt.ioff()
fig = plt.figure(figsize = (16, 12))

ax = fig.add_subplot(111, projection='3d')

R = np.array(r_array)
theta = np.array(theta_array) * np.pi / 180 + np.pi/2
phi = np.array(phi_array) * np.pi / 180

ax.set_xlim(0,100)
ax.set_ylim(-50,50)
ax.set_zlim(-50,50)

#Need to convert spherical to rectangular

ax.scatter(R * np.sin(theta) * np.cos(phi) + lateral_offset * np.sin(phi), R * np.sin(theta) * np.sin(phi) + lateral_offset * np.cos(phi), R * np.cos(theta))

plt.show()
