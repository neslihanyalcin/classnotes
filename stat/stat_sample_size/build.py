import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_sample_size.tex")
    os.system("evince stat_*.pdf")
    exit()
    
