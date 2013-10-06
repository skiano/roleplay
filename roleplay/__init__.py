# dev stuff
import resource
import time
# print 'Memory ->', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# important stuff
import os
import itertools
import multiprocessing
import numpy

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
parts = itertools.tee(processed,8)

arr = numpy.vstack(itertools.imap(rowaction, form.rows))

print len(arr)


