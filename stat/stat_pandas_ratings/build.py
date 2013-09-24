import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py  --format latex ratings.ipynb")
    os.system("pdflatex ratings.tex")
    os.system("evince ratings.pdf")
    #exit()
