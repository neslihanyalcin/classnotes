import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex karesel.tex")
    os.system("evince karesel.pdf")
    exit()
