'''
Métodos Numéricos II
 - Gabriel Freire do Vale (418788)
 - Pedro Ernesto de Oliveira Primo (418465)
'''

import cv2
from typing import Callable, List
import numpy as np

class Image:


  def __init__(self, path: str):
    '''
    Loads an image in grayscale
    '''
    self.path = path
    self.image = cv2.imread(path) # Read image
    self.original = self.image.copy()

    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    self.image = cv2.normalize(
      self.image,
      None,
      alpha=0, beta=1,
      norm_type=cv2.NORM_MINMAX,
      dtype=cv2.CV_32F
    ) # Normalize

  def __str__(self) -> str:
    return self.image.shape


  def display_treated(self) -> None:
    '''
    Displays the current image in a window.
    '''
    # Create window with image
    cv2.imshow(self.path, self.image)
    # Loop until 'Esc' is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()


  def display(self) -> None:
    '''
    Displays a comparison of the original image and the treated one
    '''
    print('Displaying images. Press ESC to exit.')
    cv2.imshow(self.path + ' (original)', self.original)
    cv2.imshow(self.path + ' (treated)', self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


  def apply_filter(self, *filter):
    '''
    Applies a filter (function) to an image
    '''
    print('Applying %s filter(s) to %s' % (len(filter), self.path))

    rows, cols = self.image.shape
    # Expands image matrix by 1 pixel in each border
    pad_img = np.pad(self.image, (1, 1), 'constant')

    for func in filter:
      for i in range(1, rows):
        for j in range(1, cols):
          pad_img[i, j] = func(pad_img, i, j) 
    
    self.image = pad_img[1:-1, 1:-1].copy()

