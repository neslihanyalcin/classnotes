import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape ode_mattuck_15.tex")
    os.system("evince ode_mattuck_15.pdf")
    exit()
