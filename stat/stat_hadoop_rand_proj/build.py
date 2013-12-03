import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_hadoop_rand_proj.tex")
    os.system("evince stat_hadoop_rand_proj.pdf")
