import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_factor.tex")
    os.system("evince stat_factor.pdf")
    exit()
