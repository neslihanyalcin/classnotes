import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex phd.tex")
    os.system("evince phd.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/phd.zip phd.pdf phd.tex build.py")
    
    
