import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py compscieng_z.ipynb -f latex")
    os.system("pdflatex compscieng_z.tex")
    os.system("evince compscieng_z.pdf")
    exit()
