import os, sys

import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex qp.tex")
    os.system("evince qp.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    os.system("zip ~/Dropbox/Public/skfiles/qp.zip qp.tex qp.py qp.pdf build.py")

