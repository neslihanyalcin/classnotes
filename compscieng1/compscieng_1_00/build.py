import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex compscieng*.tex")
    os.system("evince compscieng*.pdf")
    exit()
    
