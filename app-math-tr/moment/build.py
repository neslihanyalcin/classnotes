import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex moment.tex")
    os.system("evince moment.pdf")
    exit()
        
