import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex ml-tr.tex")
    os.system("evince ml-tr.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/ml-leastsquare.zip *.pdf ml-tr.tex ml.tex *.jpg *.bmp *.eps *.cls build.py")
    
