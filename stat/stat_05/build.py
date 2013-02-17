import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py stat_05_2.ipynb -f latex")
    os.system("pdflatex stat_05_2.tex")
    os.system("evince stat_05_2.pdf")
    exit()
