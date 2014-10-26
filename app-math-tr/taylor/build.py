import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape taylor.tex")
    os.system("evince taylor.pdf")
    exit()
