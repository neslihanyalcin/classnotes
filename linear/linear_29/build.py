import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex linear_*.tex")
    os.system("evince linear_*.pdf")
    exit()
    
