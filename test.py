import png
import itertools
import numpy


# The Scanner 
# produces an iterator
# for scanning and filtering 
# a png one row at a time
class Scanner:

  # TODO: validation?

  # f should by a valid 
  # file path to a png
  def __init__(self,fltr,f):
    self.f = f
    self.fltr = fltr
    self.load()

  # Make this an iterator
  def __iter__(self):
    return self

  # Set up an iterator and 
  # start information
  def load(self):
    img = png.Reader(self.f).asDirect()
    self.w = img[0] # width
    self.h = img[1] # height
    self.p = img[2] # pixels
    self.r = 0 # current row

  # Advance the iterator and
  # apply the filter
  def next(self):
    # if the height is exceeded 
    # loop back to the beginning 
    if(self.r >= self.h):
      self.load()
    # return the filtered row
    return self.fltr(self.p.next())

# A filter that gathers
# the positions and of non transparent pixels
# and provides data about the solids/voids
def formFilter:
  pass

# A filter that gathers color information
# for any opaque image pixels
def contentFilter:
  pass

# create a filter
def notzero(x): 
  return x != 0 

# filter for row
def getrow(row):
  alphas = row[3:][0::4]
  # for i, a in enumerate(alphas):
  #   if(a != 0):
  #     print a
  #     print row[i*4-4:i*4]

  return filter(notzero,alphas)  

# for row in itertools.imap(getrow,px[2]):
#   print len(row)


r = Scanner(getrow,'imgsrc/570px_Ingo_Oschmann_by_Plumpaquatsch1.png')


r.next()



# example of getting a 2d array
# image_2d = numpy.vstack(itertools.imap(numpy.uint16, px[2]))





# run throught the iterator from r.asDirect()
# for row in px[2]:
#   r = 0
#   g = 1
#   b = 2
#   a = 3
#   alphas = row[a:][0::4]
#   print filter(notzero,alphas)


