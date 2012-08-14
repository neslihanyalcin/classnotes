import os, sys, re

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex stat_08.tex")
    os.system("evince stat_08.pdf")
