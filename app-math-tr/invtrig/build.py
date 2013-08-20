import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex inv*.tex")
    os.system("evince inv*.pdf")
    exit()

    
