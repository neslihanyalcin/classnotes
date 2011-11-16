import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex pfrac*.tex")
    os.system("evince pfrac*.pdf")
    exit()

    
