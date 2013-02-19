import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py stat_wells.ipynb -f latex")
    os.system("pdflatex stat_wells.tex")
    os.system("evince stat_wells.pdf")
    exit()
