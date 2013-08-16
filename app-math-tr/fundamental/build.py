import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex fund*.tex")
    os.system("evince fund*.pdf")
    exit()
    
    
