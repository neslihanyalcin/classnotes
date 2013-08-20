import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex buyuk.tex")
    os.system("evince  buyuk.pdf")
    exit()
