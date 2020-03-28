from Image import Image

import math
import numpy as np

corgi = Image('images/corgi.jpg')


def box_blur(image, row, col):
  h = image[row-1, col] + image[row+1, col]
  v = image[row, col+1] + image[row, col-1]
  return (h + v)/4


def gaussian_blur(image, row, col):
  h = 2*image[row-1, col] + 2*image[row+1, col]
  v = 2*image[row, col-1] + 2*image[row, col+1]
  d = image[row-1, col+1] + image[row+1, col+1] + image[row+1, col-1] + image[row-1, col-1]
  return (h + v + d)/16


corgi.apply_filter(box_blur, 3)
corgi.display()
