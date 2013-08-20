import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex probsolve.tex")
    os.system("evince probsolve.pdf")
    exit()

if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/probsolve.zip *.jpg *.png *.lisp *.pdf probsolve.tex build.py"
    os.system(cmd)
    
    
