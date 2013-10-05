# A Collection of filter functions 
# to be used with the Scanner class

# HELPERS

def notzero(x): 
  return x != 0 

# A filter that gathers information
# about solid/void pixels in row
def formFilter(row):
  return "form row"

# A filter that gathers color information
# for any opaque image pixels
def contentFilter(row):
  return "content row"

# filter for row
# def getrow(row):
#   # start at 4th 
#   # iterate by 4s
#   alphas = row[3:][0::4]
#   # for i, a in enumerate(alphas):
#   #   if(a != 0):
#   #     print a
#   #     print row[i*4-4:i*4]

#   return filter(notzero,alphas)  

