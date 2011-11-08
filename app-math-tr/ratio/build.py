import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex ratio.tex")
    os.system("evince ratio.pdf")
    exit()

    
    
