import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex euler*.tex")
    os.system("evince euler*.pdf")
    exit()
