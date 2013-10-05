# dev stuff
import resource
import time
# print 'Memory ->', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# important stuff
import os
import itertools
import multiprocessing

# Mine
import scanner  
import director
import multitask


# get the director
d = director.minimalDirector('imgsrc')

start = time.clock()

# choose the files
files = d.choose(2)

filesChosen = time.clock()

# make scanners
form = scanner.formScanner(files[0])
content = scanner.contentScanner(files[1])

# Patch content if needed
if(form.h > content.h):
  # THIS COULD BE OFF BY ONE OR TWO
  # DO SOME SIMPLE TESTS
  l = form.h - content.h
  print "Patching content:", l
  patch = itertools.islice(itertools.count(),l)
  content.rows = itertools.chain(content.rows,patch)

def rowaction(r):
  return r

zipped = itertools.izip(content.rows,form.rows)
processed = itertools.imap(rowaction,zipped)

class Transformer:

  def __init__(self):
    self.counter = 0
    self.name = "get Length"

  def transform(self,r):
    self.counter += 1
    return len(r)

tfA = Transformer()



runner = multitask.Multimap(tfA,processed)

 # for windows stability
if __name__ == '__main__':
  tasks   = multiprocessing.Queue()
  results = multiprocessing.Queue()

  print runner(tasks, results)


