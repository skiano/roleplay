import os
import itertools
import multiprocessing
import numpy

# Load my modules

import scanner  
import director
import multitask


d = director.basicDirector('imgsrc')

# select pairs of files

pairs = d.choosePairs(2)

s = scanner.basic(pairs[1])
s.merge()








