import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex turev.tex")
    os.system("evince turev.pdf")
    exit()
