import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex ode*.tex")
    os.system("evince ode*.pdf")
    exit()
    
