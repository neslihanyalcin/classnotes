import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex rayleigh.tex")
    os.system("evince rayleigh.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/rayleigh.zip rayleigh.pdf rayleigh.tex build.py")
    
    
