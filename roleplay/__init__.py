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
d = director.basicDirector('imgsrc')

pairs = d.choosePairs(12)

print pairs




