import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex cauchy.tex")
    os.system("evince cauchy.pdf")
    exit()

