import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py fem2.ipynb -f latex")
    os.system("pdflatex fem2.tex")
    os.system("evince fem2.pdf")
    exit()
