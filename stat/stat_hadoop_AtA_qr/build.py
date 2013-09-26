import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py  --format latex stat_AtA_qr.ipynb")
    os.system("pdflatex stat_AtA_qr.tex")
    os.system("evince stat_AtA_qr.pdf")
