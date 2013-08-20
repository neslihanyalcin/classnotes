import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py patent.ipynb -f latex")
    os.system("pdflatex patent.tex")
    os.system("evince patent.pdf")
    exit()
