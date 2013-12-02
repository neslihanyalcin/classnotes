import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape spline.tex")
    os.system("evince spline.pdf")
    exit()
