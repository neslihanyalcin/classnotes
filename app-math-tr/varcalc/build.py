import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex varcalc.tex")
    os.system("evince varcalc.pdf")
    exit()
