import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_05.tex")
    os.system("evince stat_05.pdf")
    exit()
