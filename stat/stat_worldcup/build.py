import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape doc_en.tex")
    os.system("pdflatex -shell-escape stat_worldcup.tex")
    os.system("evince stat_worldcup.pdf")
    exit()
