import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex cebisev.tex")
    os.system("evince  cebisev.pdf")
    exit()
