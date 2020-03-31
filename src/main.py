from Image import Image

import math
import numpy as np


def box_blur(image, row, col):
  h = image[row-1, col] + image[row+1, col]
  v = image[row, col+1] + image[row, col-1]
  return (h + v)/4


def gaussian_blur(image, row, col):
  h = 2*image[row, col-1] + 2*image[row, col+1]
  v = 2*image[row-1, col] + 2*image[row+1, col]
  d = image[row-1, col+1] + image[row+1, col+1] + image[row+1, col-1] + image[row-1, col-1]
  return (h + v + d)/16


def edge_detection(image, row, col):
  h = image[row, col+1]/2 - image[row, col-1]/2
  v = image[row-1, col]/2 - image[row+1,col]/2
  r = abs(h + v)
  return r if r <= 1 else 1


cubes = Image('images/cubes.png')

cubes.apply_filter(box_blur, edge_detection)
cubes.display()
