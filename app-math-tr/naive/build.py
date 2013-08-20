import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py naive2.ipynb -f latex")
    os.system("pdflatex naive2.tex")
    os.system("evince naive2.pdf")
    exit()
