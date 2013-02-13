import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py lk2.ipynb -f latex")
    os.system("pdflatex lk2.tex")
    os.system("evince lk2.pdf")
    exit()
