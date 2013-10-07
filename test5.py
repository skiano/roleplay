
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

mask = np.nonzero(img)


# http://wiki.scipy.org/Tentative_NumPy_Tutorial#head-3f4d28139e045a442f78c5218c379af64c2c8c9e

print img.shape

new_image = np.zeros((img.shape[0],img.shape[1],4), np.uint8)
new_image[0:img.shape[0]/2] = (0,200,25,0)
new_image[img.shape[0]/2:img.shape[0]] = (255,40,10,0)


for y, x in np.nditer(mask):
  # old = new_image[y,x]
  new_image.itemset((y, x, 3), 255)
  # new_image[y,x] = (old[0],old[1],old[2],img[y,x])





out = join(getcwd(),'imgout',basename(testfile))
print "Out:", out
cv2.imwrite(out,new_image)

