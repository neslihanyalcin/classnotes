import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex mr_svd.tex")
    os.system("evince mr_svd.pdf")
    exit()

