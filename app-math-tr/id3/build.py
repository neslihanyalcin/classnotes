import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex  -shell-escape id3.tex")
    os.system("evince id3.pdf")
    exit()

    
    
