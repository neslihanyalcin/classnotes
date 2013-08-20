import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex lhosp*.tex")
    os.system("evince lhosp*.pdf")
    exit()        

