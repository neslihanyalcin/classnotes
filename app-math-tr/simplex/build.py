import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex simplex.tex")
    os.system("evince simplex.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/simplex.zip simplex.pdf simplex.tex *.py *.m inprogress/*")
    
