import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex cover.tex")
    os.system("evince cover.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/app-math-cover.zip *.py *.pdf cover.tex"
    os.system(cmd)
    
