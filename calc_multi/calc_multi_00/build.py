import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex calc*.tex")
    os.system("evince calc*.pdf")
    exit()
    
