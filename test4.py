
from os  import getcwd
from os  import listdir
from os.path import isfile, join, basename
from random import choice, sample

import cv2
import numpy as np

d = join(getcwd(),'imgsrc')
files = [ join(getcwd(),d,f) 
          for f in listdir(d) 
          if isfile(join(d,f)) ]

testfile = choice(files)

print testfile

# load unchanged
img = cv2.imread(testfile, cv2.CV_LOAD_IMAGE_UNCHANGED)

# extract channel
img = cv2.split(img)[3]

img = np.invert(img)

# rotate the image 180
img = np.rot90(img,2)




print img

out = join(getcwd(),'imgout',basename(testfile))

print out

cv2.imwrite(out,img)

