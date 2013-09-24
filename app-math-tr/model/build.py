import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex model.tex")
    os.system("evince model.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/model.zip *.jpg model.tex model.pdf build.py")
        
