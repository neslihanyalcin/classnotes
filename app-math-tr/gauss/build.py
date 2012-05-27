import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex gauss*.tex")
    os.system("evince gauss*.pdf")
    exit()
    
    
