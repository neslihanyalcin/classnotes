import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py fourier2.ipynb -f latex")
    os.system("pdflatex fourier2.tex")
    os.system("evince fourier2.pdf")
    exit()
