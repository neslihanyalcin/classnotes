import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape z.tex")
    os.system("evince z.pdf")
    exit()
