import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py stat_hadoop_logreg.ipynb -f latex")
    os.system("pdflatex stat_hadoop_logreg.tex")
    os.system("evince stat_hadoop_logreg.pdf")
    exit()
