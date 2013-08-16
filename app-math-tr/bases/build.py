import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex bases.tex")
    os.system("evince  bases.pdf")
    exit()
