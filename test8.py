from numpy import *
from itertools import *

class Scanner:

  def __init__(self, w, h, skip):
      self.w = w
      self.h = h
      self.r = 0
      self.c = 0
      self.skip = skip

  def __iter__(self):
      return self

  def next(self):
      pass

  def advance(self):
      pass


class Merger:

  def __init__(self,a,b):
      self.a = a
      self.b = b

  def swap(ca,cb):
      a.itemset(ca,b.item(cb))

content = arange(24).reshape(6,2,2)
form    = arange(48).reshape(3,4,4)

for i in nditer(form, op_flags=['readwrite'], order='C', flags=['external_loop']):
  print i

print form

