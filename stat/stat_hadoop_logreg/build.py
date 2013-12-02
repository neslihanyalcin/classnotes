import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex  -shell-escape  stat_hadoop_logreg.tex")
    os.system("evince stat_hadoop_logreg.pdf")
    exit()

