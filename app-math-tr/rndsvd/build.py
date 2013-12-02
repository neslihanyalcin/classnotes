import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape rndsvd.tex")
    os.system("evince rndsvd.pdf")
    exit()
