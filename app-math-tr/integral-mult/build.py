import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex integ*.tex")
    os.system("evince integ*.pdf")
    exit()
    
    
