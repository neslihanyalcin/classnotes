import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py svdrecom.ipynb -f latex")
    os.system("pdflatex svdrecom.tex")
    os.system("evince svdrecom.pdf")
    exit()
