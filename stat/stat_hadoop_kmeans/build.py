import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape kmeans.tex")
    os.system("evince kmeans.pdf")
