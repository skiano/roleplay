# A Collection of filter functions 
# to be used with the Scanner class

# HELPERS

def notzero(x): 
  return x != 0 


# FILTERS

def formFilter:
  pass

# A filter that gathers color information
# for any opaque image pixels
def contentFilter:
  pass



# filter for row
def getrow(row):
  alphas = row[3:][0::4]
  # for i, a in enumerate(alphas):
  #   if(a != 0):
  #     print a
  #     print row[i*4-4:i*4]

  return filter(notzero,alphas)  

# for row in itertools.imap(getrow,px[2]):
#   print len(row)