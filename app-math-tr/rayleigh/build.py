import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex rayleigh.tex")
    os.system("evince rayleigh.pdf")
    exit()

