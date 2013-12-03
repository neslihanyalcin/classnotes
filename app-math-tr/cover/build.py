import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex cover.tex")
    os.system("evince cover.pdf")
    exit()
