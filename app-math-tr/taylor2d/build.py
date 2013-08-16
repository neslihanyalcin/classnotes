import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex tay*.tex")
    os.system("evince tay*.pdf")
    exit()
