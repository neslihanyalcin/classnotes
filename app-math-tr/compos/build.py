import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex compos.tex")
    os.system("evince compos.pdf")
    exit()

    
    
