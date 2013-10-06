# same pattern with threads

import os, time
import threading, Queue
import copy

import time



import itertools

# A function for making iterable slices
def slices(iterable,l,n):
  groups = (l - l%n) / n
  tail = l - groups * n
  # compose groups
  slices = [ (g * n, g * n + n) for g in range(groups) ]
  # attatch tail if groups do not divide evenly
  if(tail):
    slices.append( (groups * n, l) )

  print slices 
  # make slices
  # print iterable.__copy__()

  return [itertools.islice(iterable,s[0],s[1]) for s in slices]




def fn(i):
  return i

l = itertools.imap(fn,range(9))

sliced = slices(l,9,3)

# print sliced

# for s in sliced:
#   print "slice", s
#   for i in s:
#     print i

# for i in sliced[2]:
#   print i

for i in sliced[1]:
  print i

# parts = (
#     itertools.islice(l,0,4),
#     itertools.islice(l,4,8)
#   )

# for i in parts[1]:
#   print i

# class Worker(threading.Thread):
#   def __init__(self, task_queue, result_queue):
#     super(Worker, self).__init__()
#     self.task_queue = task_queue
#     self.result_queue = result_queue

#   def run(self):
#     proc_name = self.name
#     while True:
#       next_task = self.task_queue.get()
#       if next_task is None:
#         # Poison pill means we should exit
#         # print '%s: Exiting' % proc_name
#         break
#       # print '%s: %s' % (proc_name, next_task)
#       result = next_task()
#       self.result_queue.put(result)
#     return    

# class Task:
#   def __init__(self, r):
#     self.r = r
#   def __call__(self):
#       # time.sleep(.4) # pretend to take some time to do our work
#       print self.r
#       # n = 0
#       # for i in self.r:
#       #   print i
#       #   n += 1
#       # return n
#   def __str__(self):
#       # string to represent this task 
#       return '%s * 2' % (self.r)


# if __name__ == '__main__':
#   # Establish communication queues
#   tasks = Queue.Queue()
#   results = Queue.Queue()
  
#   # Start Workers
#   num_workers = 8
#   print 'Creating %d Workers' % num_workers
#   Workers = [ Worker(tasks, results)
#                 for i in range(num_workers) ]
#   for w in Workers:
#     w.start()
  

#   # Enqueue jobs
#   for part in parts:
#     tasks.put(Task(part))
#   for i in range(num_workers):
#     tasks.put(None)
  
#   final = []

#   # Start printing results
#   num_jobs = len(parts);
#   while num_jobs:
#     r = results.get()
#     final.append(r)
#     num_jobs -= 1


# print final
