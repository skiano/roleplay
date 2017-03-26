import cv2
import numpy as np
import random

from math import floor

def getImg(path):
  return cv2.imread(path, cv2.IMREAD_UNCHANGED)

def getGrayImg(img):
  return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def getAllRegions(img, ksize = 5):
  # remove noise and thresh
  kernel = np.ones((ksize, ksize), np.uint8)
  opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
  blurred = cv2.GaussianBlur(opened, (ksize, ksize), 0)
  ret, thresh = cv2.threshold(blurred, (ksize * 2), 255, 0)
  inverted = cv2.bitwise_not(thresh)

  # get contours and inverted contours
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  contoursI, hierarchyI = cv2.findContours(inverted, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  return contours + contoursI, hierarchy

def colorContour(img, contour, cIdx):
  mask = np.zeros(gray.shape, np.uint8)
  cv2.drawContours(mask, [contour], 0, 255, -1)
  pixelpoints = np.transpose(np.nonzero(mask))

  i = random.randint(0, 255)
  a = random.randint(0, 255)
  l = float(len(pixelpoints))

  idx = 0
  for x in pixelpoints:
    img.itemset((x[0], x[1], 0), x[0] - int(idx/l*255))
    img.itemset((x[0], x[1], 1), int(idx/l*255) + x[1])
    img.itemset((x[0], x[1], 2), a)
    idx += 1
    i += 1

def drawContour(img, contour):
  cv2.drawContours(img, [contour], 0, (0,255,0), 3)

img = getImg('img/test-7.jpg')
gray = getGrayImg(img)
contours, hierarchy = getAllRegions(gray, 1)

cIdx = 0
for c in contours:
  colorContour(img, c, cIdx)
  cIdx += 1

cv2.imwrite('output/output.jpg', img)






# px = img[100,100]
# blue = img[100,100,0]
# red = img.item(100,100,2)

# print px
# print blue
# print red

# print img.shape
# print img.size
# print img.dtype


# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))

# 