import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_gauss_fusion.tex")
    os.system("evince stat_gauss_fusion.pdf")
    exit()
