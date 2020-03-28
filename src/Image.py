import cv2

import numpy as np

class Image:


  def __init__(self, path: str):
    '''
    Loads an image in grayscale
    '''
    self.path = path
    # Read image
    self.image = cv2.imread(path)
    # Convert to grayscale
    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    # Normalize
    self.image = cv2.normalize(self.image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

  def __str__(self) -> str:
    return self.image.shape


  def display(self) -> None:
    '''
    Displays the current image in a window.
    '''
    # Create window with image
    cv2.imshow(self.path, self.image)
    # Loop until 'Esc' is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()


  def apply_filter(self, filter, iterations):
    rows, cols = self.image.shape
    def_img = self.image
    pad_img = np.pad(def_img, (1, 1), 'constant')

    for k in range(iterations):
      for i in range(1, rows):
        for j in range(1, cols):
          pad_img[i, j] = filter(pad_img, i, j)
    
    self.image = pad_img[1:-1, 1:-1].copy()
