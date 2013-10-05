from png import Reader
from os  import getcwd
from os  import listdir
from os.path import isfile, join


# import directors
import minimal

class Brain:

  def __init__(self,src):
    self.src = join(getcwd(),src)
    self.files = [ self.getInfo(join(getcwd(),self.src,f)) 
                     for f in listdir(self.src) 
                     if isfile(join(self.src,f)) ]

  def getInfo(self,f):
    r = Reader(f)
    return {
      'h': r.asDirect()[1],
      'src': f
    }

def minimalDirector(src):

  return minimal.Create(Brain(src))


    # Director package