"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np
from obpng import *
"""
3 - Kwadrat
"""


def square(size, side, start):
    image = np.zeros((size, size)).astype(np.uint8)
    image[start[1]:side+start[1], start[0]:side+start[0]] = 255
    return image


"""
3 - Koło
"""


def midcircle(size):
    if size[0] > size[1]:
        radius = size[1]/4
    else:
        radius = size[0]/4
    radius = int(radius)
    print(radius)
    image = np.zeros((size)).astype(np.uint8)
    image[int(size[0]/2), int(size[1]/2)] = 255

    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if (((i - size[0]/2)**2 + (j - size[1]/2)**2) <= radius**2):
                image[i, j] = 255
    return image


"""
3 - Szachownica.
"""


def checkerboard(size):
    pass


"""
4 - Interpolacja najbliższych sąsiadów.
"""


def nn_interpolation(source, new_size):
    pass


"""
5 - Interpolacja dwuliniowa
"""


def bilinear_interpolation(source, new_size):
    pass
