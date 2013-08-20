import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex filter.tex")
    os.system("evince filter.pdf")
    exit()

if len(sys.argv) == 1 or sys.argv[1] == 'tex1':
    os.system("pdflatex kalman1.tex")
    os.system("evince kalman1.pdf")
    exit()

if len(sys.argv) == 1 or sys.argv[1] == 'tex2':
    os.system("pdflatex kalman2.tex")
    os.system("evince kalman2.pdf")
    exit()

if len(sys.argv) == 1 or sys.argv[1] == 'tex3':
    os.system("pdflatex kalman3.tex")
    os.system("evince kalman3.pdf")
    exit()

if len(sys.argv) == 1 or sys.argv[1] == 'tex4':
    os.system("pdflatex vis_track_filtering.tex")
    os.system("evince vis_track_filtering.pdf")
    exit()    
    
if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/filtering.zip *.sty *.jpg kalman*.tex vis*.tex *.png *.py *.pdf")
    
