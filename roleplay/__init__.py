import os
from scanner import create

f = os.getcwd() + "/imgsrc/1280px_ZonglerjaLj_by_Sl_Ziga2.png"
s = create.formScanner(f)

print s.next()

