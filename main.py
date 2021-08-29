import numpy as np
import cv2
import matplotlib.pyplot as plt


def draw():

    for Y in range(7):
        measure = [line.split(",") for line in open(f'{Y}.csv', 'r')]

        angles = []
        distances = []

        for x in measure:
            angles.append(float(x[1]))
            distances.append(float(x[2]))

        ang = np.array(angles)
        dist = np.array(distances)
        # ang, dist = draw(f'{Y}.csv')

        ox = np.sin(ang) * dist
        oy = np.cos(ang) * dist

        # plt.figure(figsize=(3000, 3000))
        plt.plot([oy, np.zeros(np.size(oy))], [ox, np.zeros(
            np.size(oy))], "ro-")  # from 0.0 to point ox,oy

        plt.axis("equal")

        bottom, top = plt.ylim()  # return current ylim
        plt.ylim((top, bottom))  # set ylimn to top bot
        plt.grid(True)
        plt.show()


draw()
