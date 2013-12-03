import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex compscieng_1_*.tex")
    os.system("evince compscieng_1_*.pdf")
    exit()
