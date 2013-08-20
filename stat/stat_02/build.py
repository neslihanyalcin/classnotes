import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex stat_*.tex")
    os.system("evince stat_*.pdf")
    exit()
    
