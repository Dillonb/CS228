#!/usr/bin/env python2
import Leap, sys, thread, time, random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib


matplotlib.interactive(True)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111,projection='3d')
plt.draw()

controller = Leap.Controller()
while(True):
    frame = controller.frame()
    if (frame.hands):
        print frame
