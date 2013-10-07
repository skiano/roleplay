from png     import Reader
from os      import listdir, getcwd
from os.path import isfile, join

# import director classes

import basic

class Brain:

  # __init__()
  # creates a list of file info dictionaries
  # from a src directory

  def __init__(self, src):
      self.src = join(getcwd(), src)
      self.files = [ self.getInfo( join( getcwd(), self.src, f) ) 
                       for f in listdir(self.src) 
                       if isfile( join( self.src, f) ) ]

  # getInfo()
  # takes a file path and
  # transforms it into a dictionary
  # of info

  def getInfo(self, f):
      r = Reader(f)
      return {
        'h': r.asDirect()[1],
        'src': f
      }


def basicDirector(src):
    # give basic a brain
    return basic.Create( Brain(src) )


