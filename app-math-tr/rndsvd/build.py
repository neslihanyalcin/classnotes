import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py rndsvd.ipynb -f latex")
    os.system("pdflatex rndsvd.tex")
    os.system("evince rndsvd.pdf")
    exit()
