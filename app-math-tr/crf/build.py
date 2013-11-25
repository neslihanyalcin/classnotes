import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex crf.tex")
    os.system("evince crf.pdf")
    exit()
        
