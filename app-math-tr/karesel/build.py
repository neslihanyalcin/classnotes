import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex karesel.tex")
    os.system("evince karesel.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/karesel.zip build.py karesel.tex karesel.pdf"
    os.system(cmd)
    
