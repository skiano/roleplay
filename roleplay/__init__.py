# dev stuff
import resource
import cTimer as timer

# important stuff
import os
import scanner  
import director

print 'Memory ->', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss



d = director.minimalDirector('imgsrc')

start = timer.start()

files = d.choose(2)

filesChosen = timer.checkpoint()

print files


stop = timer.stop()

print "Total time:", timer.diff(start, stop)
print "Time to choose files:", timer.diff(start, filesChosen)


# form = scanner.formScanner(f)
# content = scanner.contentScanner(f)



# d = minimalDirector('imgsrc')

# for f in d.choose(4):
#   print f




