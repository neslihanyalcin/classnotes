import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex series.tex")
    os.system("evince series.pdf")
    exit()

    
    
