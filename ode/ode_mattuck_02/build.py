import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex ode_mattuck_*.tex")
    os.system("evince ode_mattuck_*.pdf")
    exit()
    
    
