import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape eigseg.tex")
    os.system("evince eigseg.pdf")
    exit()
