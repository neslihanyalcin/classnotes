import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex cebisev.tex")
    os.system("evince  cebisev.pdf")
    exit()

if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/cebisev.zip cebisev.pdf cebisev.tex build.py"
    os.system(cmd)
