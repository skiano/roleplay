import png
import itertools
import numpy
import filters


# The Scanner 
# produces an iterator
# for scanning and filtering 
# a png one row at a time
class NewScanner:

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


def formScanner(f):
  return NewScanner(filters.formFilter,f)

def contentScanner(f):
  return NewScanner(filters.contentFilter,f)

