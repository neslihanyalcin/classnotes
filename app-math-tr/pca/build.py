import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py pca.ipynb -f latex")
    os.system("pdflatex pca.tex")
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py pcaperf.ipynb -f latex")
    os.system("pdflatex pcaperf.tex")
    os.system("evince pca.pdf")
    exit()
