import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape simplex.tex")
    os.system("evince simplex.pdf")
    exit()

