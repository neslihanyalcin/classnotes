import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex curvature.tex")
    os.system("evince curvature.pdf")
    exit()
        
if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/curvature.zip curvature.pdf curvature.tex build.py curvature-wolfram.pdf ")

