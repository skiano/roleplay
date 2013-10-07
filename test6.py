
from os  import getcwd
from os  import listdir
from os.path import isfile, join, basename
from random import choice, sample

import cv2
import numpy as np
import numpy.ma as ma

d = join(getcwd(),'imgsrc')
files = [ join(getcwd(),d,f) 
          for f in listdir(d) 
          if isfile(join(d,f)) ]

testfile = choice(files)

print "IN: ", testfile

# load unchanged
img = cv2.imread(testfile, cv2.CV_LOAD_IMAGE_UNCHANGED)
# extract channel
img = cv2.split(img)[3]
# rotate the image 180
# img = np.rot90(img,2)

# mask = np.nonzero(img)
mask = (img != 0)
# 
# indexes of non zeros
print img[np.nonzero(img)]

# print mask


# print img
# mask = ma.masked_where(img == 0, img)

# print mask


# for i in img:
#   print img

