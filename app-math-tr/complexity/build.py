import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex complexity.tex")
    os.system("evince complexity.pdf")
    exit()

if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/complexity.zip *.pdf *.tex *.jpg build.py"
    os.system(cmd)
    
    
