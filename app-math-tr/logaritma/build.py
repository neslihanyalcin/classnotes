import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape logaritma.tex")
    os.system("evince logaritma.pdf")
    exit()
    
    
