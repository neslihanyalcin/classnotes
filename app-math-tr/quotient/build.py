import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex quo*.tex")
    os.system("evince quo*.pdf")
    exit()

    
    
