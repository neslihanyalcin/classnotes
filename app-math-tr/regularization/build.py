import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py regular.ipynb -f latex")
    os.system("pdflatex regular.tex")
    os.system("evince regular.pdf")
    exit()
