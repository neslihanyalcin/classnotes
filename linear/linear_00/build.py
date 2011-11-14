import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex linear*.tex")
    os.system("evince linear*.pdf")
    exit()
    
