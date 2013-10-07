
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


def color(v):
  print v
  return (0,0,100,100)

f = np.vectorize(color)

print f(img)



out = join(getcwd(),'imgout',basename(testfile))
print "Out:", out
cv2.imwrite(out,img)





