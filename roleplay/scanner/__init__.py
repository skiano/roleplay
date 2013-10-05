import png
import itertools
import filters


# The Scanner 
# produces an iterator
# for scanning and filtering 
# a png one row at a time
class NewScanner:
  # f should by a valid 
  # file path to a png
  def __init__(self,fltr,f):
    img = png.Reader(f).asDirect()
    self.h = img[0]
    self.h = img[1]
    self.rows = itertools.imap(fltr,img[2])

def formScanner(f):
  return NewScanner(filters.formFilter,f)

def contentScanner(f):
  return NewScanner(filters.contentFilter,f)

