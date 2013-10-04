import png
import itertools
import numpy

r = png.Reader('imgsrc/570px_Ingo_Oschmann_by_Plumpaquatsch1.png')

px = r.asDirect()

img = r.read()

w = img[0]
h = img[1]
# px = img[2]

print(w)
print(h)
print(px)

def printrow(r):
  np.uint16
  print 'hey'
  return r

# image_2d = numpy.vstack(itertools.imap(numpy.uint16, px[2]))

# px[2].len

l = [0,1,2,3,4,5]

print l[0::2]

for row in px[2]:
  r = 0
  g = 1
  b = 2
  a = 3
  print len(row[a:][0::4])



# print image_2d

# for i in image_2d:
#   print i

# print(r.read()[2])