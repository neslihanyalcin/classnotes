import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py svdcluster2.ipynb -f latex")
    os.system("pdflatex svdcluster2.tex")
    os.system("evince svdcluster2.pdf")
    exit()
