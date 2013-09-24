import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex varcalc.tex")
    os.system("evince varcalc.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/varcalc.zip varcalc.tex varcalc.pdf build.py curve-length.eps curve-length.png")

