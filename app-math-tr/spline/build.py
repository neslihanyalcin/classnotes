import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex splines.tex")
    os.system("evince splines.pdf")
    exit()
