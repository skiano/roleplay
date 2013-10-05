# dev stuff
import resource
import time
# print 'Memory ->', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# important stuff
import os
import itertools

import scanner  
import director

# get the director
d = director.minimalDirector('imgsrc')

start = time.clock()

# choose the files
files = d.choose(2)

filesChosen = time.clock()

# make scanners
form = scanner.formScanner(files[0])
content = scanner.contentScanner(files[1])

# h = form.h if (form.h > content.h) else content.h
# w = form.w if (form.w > content.w) else content.w


startLoop = time.clock()

print 'Looping through scanners...'

def fn(row):
  return "pour", len(row[1]), "into",len(row[0]) 

zipped    = itertools.izip(content.rows,form.rows)
processed = itertools.imap(fn,zipped)

print processed


endLoop = time.clock()  

print "Form height:    ", form.h
print "Content height: ", content.h
print "Scan time:      ", endLoop - startLoop







stop = time.clock()

# print "==========================================="
# print "TIME"
# print "Total:   ", stop - start
# print "Choosing:", filesChosen - start
# print "Scanners:", endLoop - startLoop
# print 'Memory ->', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss










