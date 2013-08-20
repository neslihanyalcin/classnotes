import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex id3.tex")
    os.system("evince id3.pdf")
    exit()

if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/id3.zip build.py id3.pdf id3.tex *.jpg *.lisp "
    os.system(cmd)
    
    
