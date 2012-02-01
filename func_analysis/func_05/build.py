import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex func*.tex")
    os.system("evince func*.pdf")
    exit()
    
