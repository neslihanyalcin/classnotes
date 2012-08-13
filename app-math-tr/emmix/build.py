import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex emmix.tex")
    os.system("evince emmix.pdf")
    exit()
    
