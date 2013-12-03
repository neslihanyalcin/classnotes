import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex totaldiff.tex")
    os.system("evince totaldiff.pdf")
    exit()
