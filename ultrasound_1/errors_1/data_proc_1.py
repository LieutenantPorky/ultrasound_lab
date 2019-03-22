import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dataName = "output1.txt"

# input datastream from file and process to obtain data (eg strip away nonessential characters)
data = [ [float(i) for i in line[2:-6].split(',')] for line in open(dataName).read().split()]
#print(data)

# convert data from spherical to rectangular
lateral_offset = 6.3 #sensor offset - should be in info.txt

rect = []

for line in data:
    # packets are in the form [phi, theta, R]
    phi = line[0] * np.pi/180.
    theta = -1 * line[1] * np.pi/180. + np.pi/2
    R = line[2]

    x = R * np.sin(theta) * np.cos(phi) - lateral_offset * np.sin(phi)
    y = R * np.sin(theta) * np.sin(phi) + lateral_offset * np.cos(phi)
    z = R * np.cos(theta)

    rect.append([x,y,z])

#plot the rectangular coordinates

fig = plt.figure(figsize = (16, 12))
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)
ax.set_xlim(0,100)
ax.set_ylim(-50,50)
#ax.set_zlim(-50,50)

ax.set_xlabel('X axis')
ax.set_ylabel('Z axis')
#ax.set_zlabel('Z axis')

#ax.scatter([i[0] for i in rect], [i[1] for i in rect], [i[2] for i in rect])
ax.scatter([i[0] for i in rect], [i[2] for i in rect])
plt.show()
