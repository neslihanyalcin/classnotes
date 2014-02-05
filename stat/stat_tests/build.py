import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_tests.tex")
    os.system("evince stat_tests.pdf")
    exit()
    
