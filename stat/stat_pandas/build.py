import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py  --format latex div.ipynb")
    os.system("pdflatex div.tex")
    os.system("evince div.pdf")
    #exit()
