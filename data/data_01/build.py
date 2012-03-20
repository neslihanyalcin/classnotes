import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex data*.tex")
    os.system("evince data*.pdf")
    exit()
    
    
