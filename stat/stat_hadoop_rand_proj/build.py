import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py  --format latex stat_hadoop_rand_proj.ipynb")
    os.system("pdflatex stat_hadoop_rand_proj.tex")
    os.system("evince stat_hadoop_rand_proj.pdf")
