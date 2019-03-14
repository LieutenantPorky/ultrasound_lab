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

logging = False

#sensor offset is frontal distance between gyro and ultrasound in cm
sensor_offset = 0.0

#lateral sensor offset is distance to gyro on y axis (eg when mounting on holder)
lateral_offset = 8.5



while True:
    #read serial buffer up to newline character (indicates one package)
    newLine = ser.read_until()
    print(newLine)

    if logging:
        #if logging flag has been read, save data to buffers
        current = [float(i) for i in newLine.decode("utf-8")[:-2].split(',')]
        if(current[2] > 5 and current[2] < 150):
            phi = current[0] * np.pi / 180
            theta = current[1] * np.pi / 180 + np.pi/2
            R = current[2] + sensor_offset
            ax.scatter(R * np.sin(theta) * np.cos(phi) + lateral_offset * np.sin(phi), R * np.sin(theta) * np.sin(phi) + lateral_offset * np.cos(phi), R * np.cos(theta),c="g")
            fig.canvas.draw()
            #fig.canvas.flush_events()
            plt.pause(0.001)

    if newLine == b'a\r\n':
        #look for logging flag
        print("------------\nstart logging\n------------")
        logging = True
        #Initialise the plot
        plt.ion()
        fig = plt.figure(figsize = (16, 12))
        ax = fig.add_subplot(111, projection='3d')
        plt.xlabel("X")
        plt.ylabel("Y")
        ax.set_xlim(0,100)
        ax.set_ylim(-50,50)
        ax.set_zlim(-50,50)
        plt.show()
