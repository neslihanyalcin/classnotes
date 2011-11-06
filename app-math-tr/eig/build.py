import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex eig.tex")
    os.system("evince eig.pdf")
    exit()

    
    
