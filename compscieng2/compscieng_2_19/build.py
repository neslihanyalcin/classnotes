import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape compscieng*.tex")
    os.system("evince compscieng*.pdf")
    exit()
    
