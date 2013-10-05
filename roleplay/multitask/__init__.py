import multiprocessing
import itertools

# Uses the poison pill technique described here:
# http://broadcast.oreilly.com/2009/04/pymotw-multiprocessing-part-2.html

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
        print '%s: Exiting' % proc_name
        break
      print '%s: -> %s' % (proc_name, next_task)
      result = next_task()
      self.result_queue.put(result)
    return    


class Task:

  def __init__(self, item, transformer):
    self.item = item
    self.transformer = transformer

  def __call__(self):
    # print parts
    # apply the transform function to the item
    print parts[self.item]
    # return 1
    return map(self.transformer.transform, parts[self.item])

  def __str__(self):
    # string to represent this task 
    return self.transformer.name


class TeeTime:
  # The iterable will be split into pieces
  # using itertools.tee()
  def __init__(self, transformer, iterable):
    self.num_consumers = multiprocessing.cpu_count() * 2
    self.transformer = transformer
    self.parts = itertools.tee(iterable,self.num_consumers)

  # for windows stability
  # tasks and results must be made in main process
  def __call__(self, tasks, results):

    # Expose parts so that Task can use
    parts = self.parts
    global parts

    # Create consumers
    self.consumers = [ Consumer(tasks, results)
                       for i in range(self.num_consumers) ]

    # Start consumers
    for w in self.consumers:
      w.start()
      print '%s: Started' % w.name
    
    # Enqueue jobs
    for i, p in enumerate(self.parts):
      tasks.put(Task(i, self.transformer))

    for i in range(self.num_consumers):
      # Add the poison pill to each consumer
      tasks.put(None)
    
    final = []

    num_jobs = len(self.parts);
    while num_jobs:
      r = results.get()
      final.append(r)
      num_jobs -= 1

    return final





