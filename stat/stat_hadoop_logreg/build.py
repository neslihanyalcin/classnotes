import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python $HOME/Downloads/nbconvert2/nbconvert.py stat_hadoop_logreg2.ipynb --format latex")
    os.system("pdflatex stat_hadoop_logreg2.tex")
    os.system("evince stat_hadoop_logreg2.pdf")
    exit()
