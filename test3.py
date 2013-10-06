from png import Reader
from os  import getcwd
from os  import listdir
from os.path import isfile, join, basename
from random import choice, sample
from collections import defaultdict

import png
import numpy
import time
import itertools
import multiprocessing


# selecting

def getInfo(f):
    r = Reader(f)
    return {
      'h': r.asDirect()[1],
      'src': f
    }

d = join(getcwd(),'imgsrc')
files = [ getInfo(join(getcwd(),d,f)) 
          for f in listdir(d) 
          if isfile(join(d,f)) ]

def groupBySize(files, forgiveness):    
    grouped = defaultdict(list)
    for f in files:
      grouped[f['h'] - f['h'] % forgiveness].append(f)
    return grouped.items()

def choose(groups,n):
  g = choice(groups)[1]
  
  if(n >= len(g)):
    n = len(g)
  elif(n == 1):
    n = 2

  files = sample(g,n)

  if(len(files) < 2):
    return choose(n)

  # Just return the files
  return [f['src'] for f in files]


def getPairs(files,n):
  groups = groupBySize(files, 100)
  finals = []
  for i in range(n):
    choices = choose(groups,2)
    finals.append(choices[0])
    finals.append(choices[1])
  return finals



  

choices = getPairs(files,8)




# # Experiment with pool

# def cb(results):
#   print results


# def openImage(f):
#   img = png.Reader(f).asDirect()
#   return numpy.vstack(itertools.imap(numpy.uint16, img[2]))


# start = time.clock()

# if __name__ == '__main__':
#   pool_size = 2 # multiprocessing.cpu_count() * 2
#   pool = multiprocessing.Pool(processes=pool_size)
  
#   print pool

#   print len(choices), "files"
#   pool_outputs = pool.map_async(openImage, choices, callback=cb)
#   pool.close()
#   pool.join()

# end = time.clock()

# print "Elapsed:", end - start



class Consumer(multiprocessing.Process):

  def __init__(self, task_queue, result_queue):
    multiprocessing.Process.__init__(self)
    self.task_queue = task_queue
    self.result_queue = result_queue

  def run(self):
    proc_name = self.name
    while True:
      next_task = self.task_queue.get()
      if next_task is None:
        # sentinel encountered
        print '%s: Exiting' % proc_name
        break
      print '%s: %s' % (proc_name, next_task)
      result = next_task()
      self.result_queue.put(result)
    return    


class Task:
  def __init__(self, f):
    self.f = f

  def __call__(self):
    img = png.Reader(self.f).asDirect()
    return numpy.vstack(itertools.imap(numpy.uint16, img[2]))

  def __str__(self):
    # string to represent this task 
    return "Open %s" % basename(self.f)


start = time.clock()

if __name__ == '__main__':
  num_consumers = multiprocessing.cpu_count() * 2

  tasks = multiprocessing.Queue()
  results = multiprocessing.Queue()

  # Create consumers
  consumers = [ Consumer(tasks, results)
                for i in range(num_consumers) ]
  # Start consumers
  for w in consumers:
    w.start()
    print '%s: Started' % w.name
  
  # Enqueue jobs
  for f in choices:
    tasks.put(Task(f))

  for i in range(num_consumers):
    # Add the sentinel
    tasks.put(None)
  
  final = []

  num_jobs = len(choices);
  while num_jobs:
    r = results.get()
           
    print "Proccessed:", len(r), "px tall img"

    final.append(r)
    num_jobs -= 1

  # print final

end = time.clock()

print "Elapsed:", end - start
