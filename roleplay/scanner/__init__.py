import cv2
import numpy
from   operator import itemgetter

# The Scanner takes a pair of images
# and makes a new image
# using one for form and one for content

class basic():

  # __init__()
  # sort the pair by height
  # use shorter for the form
  # use taller for the content

  def __init__(self, pair):
      self.f1, self.f2 = [ f['src'] 
                            for f in 
                            sorted(pair, key=itemgetter('h')) ]

  def merge(self):
      self.form = self.getForm(self.f1)
      self.content = self.getContent(self.f2)

      print self.content.shape
      print self.form.shape

  def getContent(self,f):
      img = cv2.imread(f, cv2.CV_LOAD_IMAGE_UNCHANGED)
      return img

  def getForm(self,f):
      img = cv2.imread(f, cv2.CV_LOAD_IMAGE_UNCHANGED)
      img = cv2.split(img)[3] # extract alpha
      return img





