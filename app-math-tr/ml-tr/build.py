import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex ml-tr.tex")
    os.system("evince ml-tr.pdf")
    exit()
