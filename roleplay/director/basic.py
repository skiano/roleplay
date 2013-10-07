from collections import defaultdict
from random import sample
from random import choice

class Create:

  # __init__()
  # must be initialized with a brain
  # the brain must be a list of dictionaries
  # each dictionary contains info about a file

  def __init__(self, brain):
      self.src = brain.src
      self.groupBySize( brain.files )

  # groupBySize()
  # groups a list of file objs by 
  # the height key   
  # the height difference must
  # be less than the forgiveness

  def groupBySize(self, files, forgiveness = 100):    
      grouped = defaultdict(list)
      
      for f in files:
        grouped[f['h'] - f['h'] % forgiveness].append(f)
      
      self.files = grouped.items()

  # choose()
  # will select n images from files
  # from a random image group

  def choose(self, n = 2):
      g = choice(self.files)[1]

      if len(g) < 2:
        return self.choose(n)
      
      elif n == 1:
        n = 2

      elif n >= len(g):
        n = len(g)
    
      return sample(g,n)

  # choosePairs()
  # will execute choose() n times
  # and return a list of n pairs of files

  def choosePairs(self, n):
      return [ self.choose() for i in range(n) ]
      






