import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py spline2.ipynb -f latex")
    os.system("pdflatex spline2.tex")
    os.system("evince spline2.pdf")
    exit()
