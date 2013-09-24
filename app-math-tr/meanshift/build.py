import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py meanshift.ipynb -f latex")
    os.system("pdflatex meanshift.tex")
    os.system("evince meanshift.pdf")
    exit()
