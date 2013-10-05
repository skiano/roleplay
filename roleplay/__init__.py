import os
import scanner  
import director

f = os.getcwd() + "/imgsrc/1280px_ZonglerjaLj_by_Sl_Ziga2.png"
s = scanner.formScanner(f)

print s.h


# d = minimalDirector('imgsrc')

# for f in d.choose(4):
#   print f

# import resource
# print 'Memory ->', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

