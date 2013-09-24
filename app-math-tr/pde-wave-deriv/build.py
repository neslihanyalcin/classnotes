import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex pde_*.tex")
    os.system("evince pde_*.pdf")
    exit()
    
