import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py  --format latex kmeans.ipynb")
    os.system("pdflatex kmeans.tex")
    os.system("evince kmeans.pdf")
    #exit()
