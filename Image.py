import cv2

class Image:


  def __init__(self, path):
    '''
    Loads an image in grayscale
    '''
    self.path = path
    self.image = cv2.imread(path, 0)


  def display(self):
    '''
    Displays the current image in a window.
    '''
    cv2.imshow(self.path, self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
