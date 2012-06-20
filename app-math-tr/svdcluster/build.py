import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex svd*.tex")
    os.system("evince svd*.pdf")
    exit()
