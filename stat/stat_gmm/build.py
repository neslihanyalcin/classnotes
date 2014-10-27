import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_gmm.tex")
    os.system("evince stat_gmm.pdf")
    exit()
