#!/usr/bin/env python3

import sys
import serial
import io

print("Serial init")
ser = serial.Serial('/dev/ttyACM0', timeout = 1)
ser.baudrate = 9600

theta_array = []
r_array = []
logging = False

while len(r_array) < 50:
    newLine = ser.read_until()
    print(newLine)

    if logging:
        current = [float(i) for i in newLine.decode("utf-8")[:-2].split(',')]
        theta_array.append(current[0])
        r_array.append(current[1])

    if newLine == b'a\r\n':
        print("start logging")
        logging = True


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (16, 12))

ax = plt.subplot(111, projection='polar')
ax.set_rlim(0,100)
ax.plot(np.array(theta_array) * np.pi / 180.0, r_array, 'ko')

# plt.rlabel('Distance (m)')
# plt.thetalabel('Angle ')

plt.show()
