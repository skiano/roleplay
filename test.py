import multiprocessing
import time

# class Consumer(multiprocessing.Process):
    
#     def __init__(self, task_queue, result_queue):
#         multiprocessing.Process.__init__(self)
#         self.task_queue = task_queue
#         self.result_queue = result_queue

#     def run(self):
#         proc_name = self.name
#         while True:
#             next_task = self.task_queue.get()
#             if next_task is None:
#                 # Poison pill means we should exit
#                 print '%s: Exiting' % proc_name
#                 break
#             print '%s: %s' % (proc_name, next_task)
#             answer = next_task()
#             self.result_queue.put(answer)
#         return


# class Task(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __call__(self):
#         time.sleep(0.3) # pretend to take some time to do our work
#         return '%s * %s = %s' % (self.a, self.b, self.a * self.b)
#     def __str__(self):
#         return '%s * %s' % (self.a, self.b)


# if __name__ == '__main__':
#     # Establish communication queues
#     tasks = multiprocessing.Queue()
#     results = multiprocessing.Queue()
    
#     # Start consumers
#     num_consumers = multiprocessing.cpu_count() * 2
#     print 'Creating %d consumers' % num_consumers
#     consumers = [ Consumer(tasks, results)
#                   for i in xrange(num_consumers) ]
#     for w in consumers:
#         w.start()
    
#     # Enqueue jobs
#     num_jobs = 10
#     for i in xrange(num_jobs):
#         tasks.put(Task(i, i))
    
#     # Add a poison pill for each consumer
#     for i in xrange(num_consumers):
#         tasks.put(None)
    
#     # Start printing results
#     while num_jobs:
#         result = results.get()
#         print 'Result:', result
#         num_jobs -= 1


import itertools

def fn(i):
  return i

l = itertools.imap(fn,range(10))



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
        # Poison pill means we should exit
        # print '%s: Exiting' % proc_name
        break
      # print '%s: %s' % (proc_name, next_task)
      result = next_task()
      self.result_queue.put(result)
    return    

class Task:
  def __init__(self, r):
    self.r = r
  def __call__(self):
      time.sleep(10) # pretend to take some time to do our work
      return '%s * 2 = %s' % (self.r, self.r * 2)
  def __str__(self):
      # string to represent this task 
      return '%s * 2' % (self.r)


if __name__ == '__main__':
  # Establish communication queues
  tasks = multiprocessing.Queue()
  results = multiprocessing.Queue()
  
  # Start consumers
  num_consumers = multiprocessing.cpu_count() * 2
  print 'Creating %d consumers' % num_consumers
  consumers = [ Consumer(tasks, results)
                for i in xrange(num_consumers) ]
  for w in consumers:
    w.start()
  

  # Enqueue jobs
  num_jobs = 0;
  while True:
    try:
      r = l.next()
      tasks.put(Task(r))
      num_jobs += 1
    except:
      for i in xrange(num_consumers):
        tasks.put(None)
      break
  
  final = []

  # Start printing results
  while num_jobs:
    r = results.get()
    final.append(r)
    num_jobs -= 1


print final
