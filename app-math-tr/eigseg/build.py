import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py eigseg2.ipynb -f latex")
    os.system("pdflatex eigseg2.tex")
    os.system("evince eigseg2.pdf")
    exit()
