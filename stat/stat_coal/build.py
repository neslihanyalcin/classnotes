import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_coal.tex")
    os.system("evince stat_coal.pdf")
    exit()
