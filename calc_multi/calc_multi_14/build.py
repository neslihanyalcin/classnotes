import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex calc_multi_*.tex")
    os.system("evince calc_multi_*.pdf")
    exit()
    
    
