
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

print "IN: ", testfile

# load unchanged
img = cv2.imread(testfile, cv2.CV_LOAD_IMAGE_UNCHANGED)
# extract channel
img = cv2.split(img)[3]
# rotate the image 180
img = np.rot90(img,2)

h1, w1 = img.shape[:2]

print w1, "x", h1

blank_image = np.zeros((h1*2,w1*2), np.uint8) # 1 channel

blank_image[h1:h1*2,w1:w1*2] = (100)
blank_image[:,:w1] = (50)


# blank_image[100:1100,100:1100] = (90)

# blank_image[:w1,:h1] = (blank_image[:w1,:h1].astype(2) + img.astype(2)).clip(0,255).astype('u1')

offy = 330
offx = 130 

tmp = blank_image[offy:h1+offy,offx:w1+offx].astype('u2') + img.astype('u2')
tmp = tmp.clip(0,255).astype('u1')



blank_image[offy:h1+offy,offx:w1+offx] = tmp



# np.add(blank_image,img.reshape((1200, 1200)))

blank_image = np.rot90(blank_image,2)

# blank_image = img * blank_image

out = join(getcwd(),'imgout',basename(testfile))
print "Out:", out

cv2.imwrite(out,blank_image)

