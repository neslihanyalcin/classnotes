import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex poldiv.tex")
    os.system("evince poldiv.pdf")
    exit()

    
    
