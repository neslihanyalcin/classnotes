import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py svm2.ipynb -f latex")
    os.system("pdflatex svm2.tex")
    os.system("evince svm2.pdf")
    exit()
