import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex mr_svd_2.tex")
    os.system("evince mr_svd_2.pdf")
    exit()

