import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py level2.ipynb -f latex")
    os.system("pdflatex level2.tex")
    os.system("evince level2.pdf")
    exit()
