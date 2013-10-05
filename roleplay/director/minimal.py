from collections import defaultdict
from random import sample
from random import choice

class Create:
  
  def __init__(self, brain):
    self.files = self.groupBySize(brain.files,100)
    self.src   = brain.src

  def groupBySize(self, files, forgiveness):    
    grouped = defaultdict(list)
    
    for f in files:
      grouped[f['h'] - f['h'] % forgiveness].append(f)

    return grouped.items()

  def choose(self, n):
    g = choice(self.files)[1]
    
    if(n >= len(g)):
      n = len(g)
    elif(n == 1):
      n = 2

    files = sample(g,n)

    if(len(files) < 2):
      return self.choose(n)

    # Just return the files
    return [f['src'] for f in files]






