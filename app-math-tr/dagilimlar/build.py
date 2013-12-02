import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape dagilimlar.tex")
    os.system("evince dagilimlar.pdf")
    exit()
