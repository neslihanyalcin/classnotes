import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py logreg.ipynb -f latex")
    os.system("pdflatex logreg.tex")
    os.system("evince logreg.pdf")
    exit()
