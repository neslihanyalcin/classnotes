import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py dagilimlar2.ipynb -f latex")
    os.system("pdflatex dagilimlar2.tex")
    os.system("evince dagilimlar2.pdf")
    exit()
