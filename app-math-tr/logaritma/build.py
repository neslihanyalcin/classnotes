import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex logaritma.tex")
    os.system("evince logaritma.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/logaritma.zip logaritma.pdf logaritma.tex build.py *.jpg")
    
    
