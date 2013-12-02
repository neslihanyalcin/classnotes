import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape mixbern.tex")
    os.system("evince mixbern.pdf")
    exit()
