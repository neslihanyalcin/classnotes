import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py heat2.ipynb -f latex")
    os.system("pdflatex heat2.tex")
    os.system("evince heat2.pdf")
    exit()
