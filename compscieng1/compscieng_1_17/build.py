import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape compscieng_1_17.tex")
    os.system("evince compscieng_1_17.pdf")
    exit()
